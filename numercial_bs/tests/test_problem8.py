import pytest
from src.problem8 import calculate


class TestBasicCalculator:
    def test_simple_addition(self):
        assert calculate("1 + 1") == 2

    def test_simple_subtraction(self):
        assert calculate("3 - 1") == 2

    def test_mixed_ops(self):
        assert calculate(" 2-1 + 2 ") == 3

    def test_parentheses(self):
        assert calculate("(1+(4+5+2)-3)+(6+8)") == 23

    def test_nested_parentheses(self):
        assert calculate("((1+2)+(3+4))") == 10

    def test_single_number(self):
        assert calculate("42") == 42

    def test_spaces_everywhere(self):
        assert calculate("  3  +  4  ") == 7

    def test_unary_minus(self):
        assert calculate("-1") == -1

    def test_unary_minus_with_parens(self):
        assert calculate("-(3+2)") == -5

    def test_unary_minus_complex(self):
        assert calculate("- (3 + (4 + 5))") == -12

    def test_multi_digit_numbers(self):
        assert calculate("100 + 200") == 300

    def test_subtraction_chain(self):
        assert calculate("10 - 3 - 2 - 1") == 4

    def test_parens_change_order(self):
        assert calculate("10 - (3 - 2 - 1)") == 10

    def test_zero(self):
        assert calculate("0") == 0

    def test_nested_unary(self):
        assert calculate("1 - (-2)") == 3

    def test_large_expression(self):
        assert calculate("1+2+3+4+5+6+7+8+9+10") == 55
