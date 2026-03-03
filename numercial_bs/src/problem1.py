"""
Problem 1: Run-Length Encoding (Pure Python)
============================================
~8 minutes | No numpy/pandas allowed

Run-length encoding compresses consecutive repeated elements into (value, count) pairs.

Example:
    [1, 1, 1, 2, 2, 3, 1, 1] -> [(1, 3), (2, 2), (3, 1), (1, 2)]

Implement TWO functions:

1. encode(data: list) -> list[tuple[any, int]]
   - Takes a list and returns a list of (value, count) tuples
   - Empty list returns empty list

2. decode(encoded: list[tuple[any, int]]) -> list
   - Takes the encoded representation and returns the original list
   - Empty list returns empty list

Constraint: Do NOT use any imports. Pure Python only.
"""


def encode(data: list) -> list[tuple]:
    rle = []
    if data:
        current_val = data[0]
        current_count = 0
        for d in data:
            if current_val != d:
                rle.append((current_val, current_count))
                current_val = d
                current_count = 1
            else:
                current_count += 1
        rle.append((current_val, current_count))
    return rle


def decode(encoded: list[tuple]) -> list:
    decoded = []
    for k,v in encoded:
        to_add = [k]*v
        decoded.extend(to_add)
    return decoded
