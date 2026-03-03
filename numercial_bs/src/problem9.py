"""
Problem 9: Basic Calculator II (Canva Interview Question)
==========================================================
~10 minutes | Pure Python, no eval()

Given a string s representing an expression with operator precedence,
evaluate it and return the result.

The expression string contains:
    - Non-negative integers
    - '+', '-', '*', '/' operators
    - Spaces (should be ignored)
    - NO parentheses

Integer division should truncate toward zero:
    7 / 2 = 3  (not 3.5)
    -7 / 2 = -3  (truncate toward zero, not floor)

Operator precedence:
    - '*' and '/' are evaluated before '+' and '-'
    - Operators of the same precedence are evaluated left to right

Implement:
    calculate_ii(s: str) -> int

Examples:
    calculate_ii("3+2*2") -> 7        (2*2=4, then 3+4=7)
    calculate_ii(" 3/2 ") -> 1        (integer division)
    calculate_ii(" 3+5 / 2 ") -> 5    (5/2=2, then 3+2=5)

Constraint: Do NOT use eval() or compile(). No external imports.
Hint: Process * and / immediately, defer + and - to a stack.
"""


def calculate_ii(s: str) -> int:
    raise NotImplementedError
