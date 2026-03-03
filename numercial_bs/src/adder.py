import pandas as pd
import numpy as np

   
def simple_add(numbers: list[float]) -> float:
    return sum(numbers)


def column_add(df: pd.DataFrame, column: str) -> float:
    return df[column].sum()


def array_add(arr: np.array) -> float:
    return np.sum(arr)