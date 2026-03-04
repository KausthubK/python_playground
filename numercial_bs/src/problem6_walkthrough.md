# Problem 6 Walkthrough: Thread-Safe Bounded Buffer & Parallel Sum

## Part 1: BoundedBuffer (Producer-Consumer Queue)

### Core Pattern: `threading.Condition`

A `Condition` wraps a `Lock` and adds the ability to **wait** for a state change and **notify** other threads when state changes.

```python
self.condition = threading.Condition()

# Producer (put)
with self.condition:              # acquires the lock
    while self.size() == capacity:
        self.condition.wait()     # releases lock, sleeps until notified
    self._queue.append(item)
    self.condition.notify()       # wakes one waiting thread

# Consumer (get)
with self.condition:
    while self.size() == 0:
        self.condition.wait()
    item = self._queue.popleft()
    self.condition.notify()
    return item
```

### Why `while` not `if`?

```python
# WRONG
if self.size() == capacity:
    self.condition.wait()

# RIGHT
while self.size() == capacity:
    self.condition.wait()
```

**Spurious wakeups**: a thread can be woken even when no `notify()` was called (OS-level behavior). The `while` loop re-checks the condition after waking. Also, with multiple producers, another producer might fill the buffer between your `notify()` and your re-acquisition of the lock.

### Why everything must be inside `with self.condition`?

```python
# WRONG - RuntimeError: cannot notify on un-acquired lock
with self.condition:
    while self.size() == self._capacity:
        self.condition.wait()
self._queue.append(item)     # outside lock = race condition
self.condition.notify()      # outside lock = RuntimeError
```

Both the mutation (`append`/`popleft`) and the `notify()` must happen while holding the lock. Otherwise:
- Two threads could `append` simultaneously, corrupting the deque
- `notify()` requires the lock to be held (Python enforces this)

### Alternative: Semaphore-based approach

```python
class BoundedBuffer:
    def __init__(self, capacity):
        self._queue = deque()
        self._lock = threading.Lock()
        self._empty_slots = threading.Semaphore(capacity)  # starts at capacity
        self._filled_slots = threading.Semaphore(0)        # starts at 0

    def put(self, item):
        self._empty_slots.acquire()   # blocks if no empty slots
        with self._lock:
            self._queue.append(item)
        self._filled_slots.release()  # signal: one more item available

    def get(self):
        self._filled_slots.acquire()  # blocks if no items
        with self._lock:
            item = self._queue.popleft()
        self._empty_slots.release()   # signal: one more slot available
        return item
```

Two semaphores act as counters — one tracks empty slots, one tracks filled slots. Arguably cleaner because there's no `while` loop or spurious wakeup concern.

### `notify()` vs `notify_all()`

- `notify()` wakes **one** waiting thread — sufficient here because each put/get only frees one slot/item
- `notify_all()` wakes **all** waiting threads — needed when a state change could unblock multiple waiters (e.g., "shutdown" signal)

---

## Part 2: thread_safe_sum (Threading)

### Pattern: shared results list, no lock needed

```python
chunks = chunk_input(numbers, num_threads)
results = [0] * len(chunks)

def _worker(chunk, index):
    results[index] = sum(chunk)   # each thread writes its own index

threads = [threading.Thread(target=_worker, args=(chunk, i))
           for i, chunk in enumerate(chunks)]

for t in threads:
    t.start()     # launch all threads
for t in threads:
    t.join()      # wait for all threads

return sum(results)
```

**Why no lock?** Each thread writes to a **different index** — no shared mutation. If threads were appending to the same list, you'd need a lock.

**Why separate start/join loops?** If you did `start(); join()` in one loop, each thread would finish before the next starts — sequential execution, no parallelism.

### The GIL problem

The GIL (Global Interpreter Lock) ensures only one thread executes Python bytecode at a time. For CPU-bound work like `sum()`, threading gives **zero speedup** — you just add thread management overhead.

**When threading helps:** I/O-bound work (network calls, file reads, DB queries). While a thread waits on I/O, it **releases the GIL**, letting other threads run. That's why BoundedBuffer is a legitimate threading use case — producers might be fetching from APIs.

---

## Part 3: multi_pool_sum (Multiprocessing)

### Pattern: Pool.map

```python
from multiprocessing import Pool

def _pool_worker(chunk):      # MUST be at module level (pickle requirement)
    return sum(chunk)

def multi_pool_sum(numbers, num_workers):
    chunks = chunk_input(numbers, num_workers)
    with Pool(processes=num_workers) as pool:
        partial_sums = pool.map(_pool_worker, chunks)
    return sum(partial_sums)
```

**Module-level worker:** `multiprocessing` uses `pickle` to serialize the function and send it to worker processes. Lambdas, closures, and nested functions can't be pickled.

**Each process gets its own GIL** — so CPU-bound work actually runs in parallel.

---

## Benchmark: 1M integers, 4 workers/threads

```
plain sum():          7.20 ms
thread_safe_sum:     16.47 ms  (2.3x slower)
multi_pool_sum:      74.13 ms  (10.3x slower)
```

### Why threading is slower than single-threaded
GIL means threads run sequentially anyway. You pay thread creation + join overhead for nothing.

### Why multiprocessing is even worse here
The 1M integers must be **pickled → copied via IPC → unpickled** in each worker process. That serialization cost dwarfs the `sum()` computation.

### When multiprocessing wins
When **computation time >> serialization time**:
- Image processing (send file path, not pixels)
- ML training batches
- Monte Carlo simulations
- Any task taking seconds per chunk, not microseconds

Rule of thumb: if the work per chunk takes < 100ms, the IPC overhead probably isn't worth it.

---

## Threading vs Multiprocessing Summary

| | `threading` | `multiprocessing` |
|---|---|---|
| GIL | Shared (one thread at a time) | Separate per process |
| CPU-bound speedup | None | Real parallelism |
| Memory | Shared (cheap) | Copied (expensive IPC via pickle) |
| Overhead | Low (microseconds) | High (process spawn + serialization) |
| Best for | I/O-bound, shared state | CPU-bound, independent work |
| Data sharing | Direct (with locks) | Via pickle/IPC (Queue, Pipe, shared memory) |
| Worker function | Can be nested/lambda | Must be module-level (picklable) |

---

## Interview Q&A

### Q1: Why use `while` instead of `if` before `wait()`?

Spurious wakeups — the OS can wake a thread without `notify()` being called. Also, with multiple producers/consumers, another thread might change the state between `notify()` and your re-acquisition of the lock. The `while` loop re-checks the condition after every wakeup.

### Q2: Your `size()` method reads `len(self._queue)` without acquiring the lock. Is that safe?

It's safe **when called from within `put()`/`get()`** because those already hold the lock. But calling `size()` externally from another thread could give a stale value — the size might change between reading it and acting on it. For a truly thread-safe external `size()`, you'd wrap it in `with self.condition`.

### Q3: Why is `_pool_worker` defined at module level, not inside `multi_pool_sum`?

`multiprocessing.Pool.map` uses `pickle` to serialize the function for IPC to worker processes. Nested functions, lambdas, and closures cannot be pickled — you get `AttributeError: Can't pickle local object`. Module-level functions are picklable by reference (just their qualified name is sent).

### Q4: How would you actually speed up a sum of 1M integers in Python?

- **NumPy**: `np.sum(np.array(numbers))` — runs in C, no Python loop overhead, ~50x faster than `sum()`
- **math.fsum** for floating point (more accurate, not faster)
- At extreme scale: chunked NumPy arrays + multiprocessing (but NumPy alone handles 1M trivially)

The real lesson: **don't parallelize cheap operations**. Optimize the single-threaded version first (use C extensions like NumPy), then only parallelize if it's still too slow.

### Q5: What's `concurrent.futures` and when would you use it over raw `threading`/`multiprocessing`?

`concurrent.futures` provides a unified API (`ThreadPoolExecutor` / `ProcessPoolExecutor`) with:
- `executor.map()` — like `Pool.map` but works for both threads and processes
- `executor.submit()` — returns a `Future` object you can check/cancel
- Context manager support for cleanup

It's the **preferred high-level API** for production code. Raw `threading.Thread` is for when you need fine-grained control (like BoundedBuffer).
