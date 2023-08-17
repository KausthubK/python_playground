from dataframe_validation.schemas.item_with_group_name import ItemWithGroupNameSchema, ItemsGroupedByName
from pydantic import validate_arguments
import pandera as pa
import pandas as pd

@validate_arguments
def group_by_group_name(df: pa.typing.DataFrame[ItemWithGroupNameSchema]) -> pa.typing.DataFrame[ItemsGroupedByName]:
    return df.groupby("group_name").agg(list).reset_index()

