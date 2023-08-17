import pandas as pd
from typing import List
from dataframe_validation.operations import grouping_operations

good_input_df = pd.DataFrame({
    "id": ["a", "b", "c", "d"],
    "val_1": ["foo", "bar", "baz", "qux"],
    "group_name": ["A", "B", "C", "A"]
})

out_df = grouping_operations.group_by_group_name(good_input_df)

print(out_df)

def explain(name: str, vals: List):
    print(f"{name}: {vals}")

listified_prints = [
    explain(name=row.group_name, vals=row.val_1) for idx, row in out_df.iterrows()
]