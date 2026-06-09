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
    expression = s.replace(' ', '')
    i = 0
    stack = []
    current_num = 0
    prev_op = '+'  # treat first number as "+num"

    while i < len(expression):
        ch = expression[i]

        if ch.isnumeric():
            j = i
            while j < len(expression) and expression[j].isnumeric():
                j += 1
            current_num = int(expression[i:j])
            i = j
        else:
            i += 1

        # apply when we hit an operator or end of expression
        if not ch.isnumeric() or i == len(expression):
            if prev_op == '+':
                stack.append(current_num)
            elif prev_op == '-':
                stack.append(-current_num)
            elif prev_op == '*':
                stack.append(stack.pop() * current_num)
            elif prev_op == '/':
                stack.append(int(stack.pop() / current_num))
            prev_op = ch
            current_num = 0

    return sum(stack)
