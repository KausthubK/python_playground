import pandera as pa
from pandera.typing import Series
from pydantic import BaseModel

class ItemSchema(pa.DataFrameModel):
    id: Series[str] = pa.Field()
    version: Series[str] = pa.Field()

class Item(BaseModel):
    id: str
    version: str

class ListOfItemsSchema(pa.DataFrameModel):
    items: Series[ItemSchema] = pa.Field()