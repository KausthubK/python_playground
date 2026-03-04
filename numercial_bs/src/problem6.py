"""
Problem 6: Thread-Safe Bounded Buffer (Concurrency)
=====================================================
~10 minutes | threading module only

Implement a thread-safe bounded buffer (producer-consumer queue) that multiple
threads can safely read from and write to concurrently.

class BoundedBuffer:
    def __init__(self, capacity: int)
        - Create a buffer that holds at most `capacity` items

    def put(self, item) -> None
        - Add an item to the buffer
        - If the buffer is full, BLOCK until space is available

    def get(self) -> any
        - Remove and return the oldest item (FIFO order)
        - If the buffer is empty, BLOCK until an item is available

    def size(self) -> int
        - Return current number of items in the buffer (thread-safe)

Requirements:
    - Use threading.Lock, threading.Condition, or threading.Semaphore
      (your choice — pick what's appropriate)
    - Must be safe for concurrent access from multiple producer/consumer threads
    - put() must block (not raise) when full
    - get() must block (not raise) when empty
    - FIFO ordering

Also implement:

    def thread_safe_sum(numbers: list[int], num_threads: int) -> int
        - Split `numbers` across `num_threads` worker threads
        - Each thread computes a partial sum
        - Combine the results and return the total
        - Must actually use threads (not just call sum())
        - This demonstrates: why would you use multiprocessing instead of
          threading for CPU-bound work in Python? (GIL)

Allowed imports: threading, collections.deque
"""

import threading
from collections import deque
from multiprocessing import Pool


class BoundedBuffer:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._queue = deque(maxlen=capacity)
        self.condition = threading.Condition()

    def put(self, item) -> None:
        """- Add an item to the buffer
        - If the buffer is full, BLOCK until space is available"""
        with self.condition:
            while self.size() == self._capacity:
                self.condition.wait()
            self._queue.append(item)
            self.condition.notify()
        return

    def get(self):
        with self.condition:
            while self.size() == 0:
                self.condition.wait()
            item = self._queue.popleft()
            self.condition.notify()
            return item

    def size(self) -> int:
        return len(self._queue)
    

def chunk_input(numbers: list[int], num_parallel: int):
    chunk_size = len(numbers) // num_parallel or 1
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
    return chunks


def thread_safe_sum(numbers: list[int], num_threads: int) -> int:
    """
        - Split `numbers` across `num_threads` worker threads
        - Each thread computes a partial sum
        - Combine the results and return the total
        - Must actually use threads (not just call sum())
        - This demonstrates: why would you use multiprocessing instead of
          threading for CPU-bound work in Python? (GIL)
    """
    chunks = chunk_input(numbers=numbers, num_parallel=num_threads)
    results = [0] * len(chunks)
    
    def _worker(chunk, index):
        results[index] = sum(chunk)
    
    threads = [threading.Thread(target=_worker, args=(chunk, i)) for i, chunk in enumerate(chunks)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(results)


def _pool_worker(chunk: list[int]) -> int:
    return sum(chunk)


def multi_pool_sum(numbers: list[int], num_workers: int) -> int:
    """
    Extension: now let's use multiprocessing to do this properly.
    """
    chunks = chunk_input(numbers=numbers, num_parallel=num_workers)
    with Pool(processes=num_workers) as pool:
        partial_sums = pool.map(_pool_worker, chunks)
    return sum(partial_sums)
