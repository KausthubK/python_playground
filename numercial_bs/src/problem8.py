"""
Problem 8: Basic Calculator (Canva Interview Question)
=======================================================
~10 minutes | Pure Python, no eval()

Given a string s representing a valid expression, implement a basic calculator
to evaluate it and return the result.

The expression string may contain:
    - Non-negative integers
    - '+' and '-' operators
    - '(' and ')' parentheses
    - Spaces (should be ignored)

The '-' operator CAN be unary (e.g., "-1" or "(-2+3)").
The '+' operator is NOT unary.

Implement:
    calculate(s: str) -> int

Examples:
    calculate("1 + 1") -> 2
    calculate(" 2-1 + 2 ") -> 3
    calculate("(1+(4+5+2)-3)+(6+8)") -> 23
    calculate("- (3 + (4 + 5))") -> -12

Constraint: Do NOT use eval() or compile(). No external imports.
Hint: Use a stack to handle parentheses.
"""


def calculate(s: str) -> int:
    raise NotImplementedError
