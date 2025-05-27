import pandas as pd
import pytest


@pytest.fixture(scope="function")
def good_input_df():
    return pd.DataFrame({
        "id": ["a", "b", "c", "d"],
        "val_1": ["foo", "bar", "baz", "qux"],
        "group_name": ["A", "B", "C", "A"]
    })


@pytest.fixture(scope="function")
def good_output_df():
    return pd.DataFrame({
        "group_name": ["A", "B", "C"],
        "id": [["a", "d"], ["b"], ["c"]],
        "val_1": [["foo", "qux"], ["bar"], ["baz"]],
    })


@pytest.fixture(scope="function")
def bad_input_df():
    return pd.DataFrame({
        "id": ["a", "b", "c", "d"],
        "val_1": ["foo", "bar", "baz", "qux"],
        "group_name": ["A", "B", "D", "A"]
    })
