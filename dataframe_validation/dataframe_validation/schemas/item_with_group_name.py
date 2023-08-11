import pandas as pd
import pandera as pa
from pandera.typing import Series, DataFrame
from typing import List
import pydantic

class ItemWithGroupNameSchema(pa.DataFrameModel):
    id: Series[str] = pa.Field(unique=True)
    val_1: Series[str] = pa.Field()
    group_name: Series[str] = pa.Field(isin=["A", "B", "C"])

class ItemsGroupedByName(pa.DataFrameModel):
    group_name: Series[str] = pa.Field(isin=["A", "B", "C"])
    id: Series[List[str]] = pa.Field()
    val_1: Series[List[str]] = pa.Field()
