import pytest
from src.problem9 import calculate_ii


class TestBasicCalculatorII:
    def test_addition(self):
        assert calculate_ii("3+2") == 5

    def test_subtraction(self):
        assert calculate_ii("10-3") == 7

    def test_multiplication(self):
        assert calculate_ii("3*4") == 12

    def test_division(self):
        assert calculate_ii("10/3") == 3

    def test_mul_before_add(self):
        assert calculate_ii("3+2*2") == 7

    def test_div_before_sub(self):
        assert calculate_ii("10-6/2") == 7

    def test_simple_division_with_spaces(self):
        assert calculate_ii(" 3/2 ") == 1

    def test_mixed_precedence(self):
        assert calculate_ii(" 3+5 / 2 ") == 5

    def test_chained_multiplication(self):
        assert calculate_ii("2*3*4") == 24

    def test_chained_division(self):
        assert calculate_ii("100/10/2") == 5

    def test_all_operators(self):
        assert calculate_ii("2+3*4-6/2") == 11  # 2+12-3=11

    def test_single_number(self):
        assert calculate_ii("42") == 42

    def test_multi_digit(self):
        assert calculate_ii("100+200") == 300

    def test_truncate_toward_zero(self):
        """Integer division truncates toward zero."""
        assert calculate_ii("7/2") == 3
        assert calculate_ii("1/2") == 0

    def test_subtraction_then_multiply(self):
        assert calculate_ii("5-2*3") == -1

    def test_complex_expression(self):
        assert calculate_ii("1+2*3-4/2+5") == 10  # 1+6-2+5=10

    def test_spaces(self):
        assert calculate_ii("  12  +  8  /  4  ") == 14

    def test_zero_division_result(self):
        assert calculate_ii("1/3") == 0

    def test_large_numbers(self):
        assert calculate_ii("1000*1000") == 1000000
