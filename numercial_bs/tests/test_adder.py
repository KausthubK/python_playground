import pytest
import pandas as pd
import numpy as np

from src.adder import simple_add, column_add, array_add


common_params = pytest.mark.parametrize(
    argnames=["input_vals", "expected_sum"],
    argvalues=[
        ([1, -1], 0),
        ([1, 0], 1),
        ([3, 4], 7),
    ]
)


@common_params(
    argnames=["input_vals", "expected_sum"],
    argvalues=[
        ([1, -1], 0),
        ([1, 0], 1),
        ([3, 4], 7),
    ]
)
def test_simple_add(input_vals, expected_sum):
    assert simple_add(input_vals) == expected_sum


@common_params(
    argnames=["input_vals", "expected_sum"],
    argvalues=[
        ([1, -1], 0),
        ([1, 0], 1),
        ([3, 4], 7),
    ]
)
def test_column_add(input_vals, expected_sum):
    df = pd.DataFrame({"input": input_vals})
    assert column_add(df, column="input") == expected_sum



@common_params(
    argnames=["input_vals", "expected_sum"],
    argvalues=[
        ([1, -1], 0),
        ([1, 0], 1),
        ([3, 4], 7),
    ]
)
def test_array_add(input_vals, expected_sum):
    arr = np.array(input_vals)
    assert array_add(arr) == expected_sum
