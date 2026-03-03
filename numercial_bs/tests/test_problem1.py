import pytest
from src.problem1 import encode, decode


class TestEncode:
    def test_basic(self):
        assert encode([1, 1, 1, 2, 2, 3]) == [(1, 3), (2, 2), (3, 1)]

    def test_no_repeats(self):
        assert encode([1, 2, 3, 4]) == [(1, 1), (2, 1), (3, 1), (4, 1)]

    def test_all_same(self):
        assert encode([5, 5, 5, 5]) == [(5, 4)]

    def test_empty(self):
        assert encode([]) == []

    def test_single_element(self):
        assert encode([42]) == [(42, 1)]

    def test_strings(self):
        assert encode(["a", "a", "b", "b", "b", "a"]) == [("a", 2), ("b", 3), ("a", 1)]

    def test_alternating(self):
        assert encode([1, 2, 1, 2, 1]) == [(1, 1), (2, 1), (1, 1), (2, 1), (1, 1)]


class TestDecode:
    def test_basic(self):
        assert decode([(1, 3), (2, 2), (3, 1)]) == [1, 1, 1, 2, 2, 3]

    def test_empty(self):
        assert decode([]) == []

    def test_single(self):
        assert decode([(7, 1)]) == [7]

    def test_strings(self):
        assert decode([("a", 2), ("b", 3)]) == ["a", "a", "b", "b", "b"]


class TestRoundTrip:
    @pytest.mark.parametrize("original", [
        [1, 1, 1, 2, 2, 3, 1, 1],
        [1],
        [],
        ["x", "x", "y", "z", "z", "z"],
        [True, True, False, False, True],
    ])
    def test_encode_decode_roundtrip(self, original):
        assert decode(encode(original)) == original
