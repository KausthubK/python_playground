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


class BoundedBuffer:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def put(self, item) -> None:
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError


def thread_safe_sum(numbers: list[int], num_threads: int) -> int:
    raise NotImplementedError
