import pyarrow as pa

id = pa.field('id', pa.string(), nullable=False)
version = pa.field('version', pa.string(), nullable=False)

item_schema = pa.schema([id, version])
item_sub_schema = pa.schema([id])

item = pa.struct([id, version])

list_of_items_schema = pa.schema(
    [
        pa.field("items", pa.list_(item), nullable=False),
    ]
)