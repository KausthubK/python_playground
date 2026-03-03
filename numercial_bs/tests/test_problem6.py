import threading
import time
import pytest
from src.problem6 import BoundedBuffer, thread_safe_sum


class TestBoundedBufferBasics:
    def test_put_and_get_single(self):
        buf = BoundedBuffer(capacity=5)
        buf.put(42)
        assert buf.get() == 42

    def test_fifo_order(self):
        buf = BoundedBuffer(capacity=5)
        for i in range(5):
            buf.put(i)
        for i in range(5):
            assert buf.get() == i

    def test_size(self):
        buf = BoundedBuffer(capacity=5)
        assert buf.size() == 0
        buf.put("a")
        assert buf.size() == 1
        buf.put("b")
        assert buf.size() == 2
        buf.get()
        assert buf.size() == 1

    def test_size_after_fill_and_drain(self):
        buf = BoundedBuffer(capacity=3)
        buf.put(1)
        buf.put(2)
        buf.put(3)
        assert buf.size() == 3
        buf.get()
        buf.get()
        buf.get()
        assert buf.size() == 0


class TestBoundedBufferConcurrency:
    def test_producer_consumer(self):
        """Multiple producers and consumers should not lose or duplicate items."""
        buf = BoundedBuffer(capacity=10)
        produced = []
        consumed = []
        lock = threading.Lock()
        num_items = 100

        def producer(start, count):
            for i in range(start, start + count):
                buf.put(i)
                with lock:
                    produced.append(i)

        def consumer(count):
            for _ in range(count):
                item = buf.get()
                with lock:
                    consumed.append(item)

        # 4 producers, each producing 25 items
        producers = [threading.Thread(target=producer, args=(i * 25, 25)) for i in range(4)]
        # 4 consumers, each consuming 25 items
        consumers = [threading.Thread(target=consumer, args=(25,)) for i in range(4)]

        for t in producers + consumers:
            t.start()
        for t in producers + consumers:
            t.join(timeout=5)

        assert sorted(consumed) == sorted(produced)
        assert len(consumed) == num_items
        assert buf.size() == 0

    def test_blocking_on_full(self):
        """put() should block when buffer is full, not raise."""
        buf = BoundedBuffer(capacity=2)
        buf.put(1)
        buf.put(2)
        # Buffer is now full. put() in a thread should block.
        put_completed = threading.Event()

        def blocked_put():
            buf.put(3)
            put_completed.set()

        t = threading.Thread(target=blocked_put)
        t.start()
        # Give the thread a moment — it should NOT complete yet
        time.sleep(0.1)
        assert not put_completed.is_set(), "put() should block when buffer is full"
        # Now consume one item to unblock
        buf.get()
        t.join(timeout=2)
        assert put_completed.is_set(), "put() should complete after space is freed"

    def test_blocking_on_empty(self):
        """get() should block when buffer is empty, not raise."""
        buf = BoundedBuffer(capacity=5)
        get_completed = threading.Event()
        result = []

        def blocked_get():
            item = buf.get()
            result.append(item)
            get_completed.set()

        t = threading.Thread(target=blocked_get)
        t.start()
        time.sleep(0.1)
        assert not get_completed.is_set(), "get() should block when buffer is empty"
        buf.put(99)
        t.join(timeout=2)
        assert get_completed.is_set(), "get() should complete after item is available"
        assert result == [99]


class TestThreadSafeSum:
    def test_basic(self):
        assert thread_safe_sum([1, 2, 3, 4, 5], num_threads=2) == 15

    def test_single_thread(self):
        assert thread_safe_sum([10, 20, 30], num_threads=1) == 60

    def test_more_threads_than_items(self):
        assert thread_safe_sum([5, 5], num_threads=4) == 10

    def test_empty_list(self):
        assert thread_safe_sum([], num_threads=2) == 0

    def test_large_list(self):
        numbers = list(range(1000))
        expected = sum(numbers)
        assert thread_safe_sum(numbers, num_threads=4) == expected

    def test_negative_numbers(self):
        assert thread_safe_sum([-1, -2, 3, 4], num_threads=2) == 4
