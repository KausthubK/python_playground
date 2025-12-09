# Dataframes

There are a bunch of dataframe libraries in Python. I'm trying to get more familiar with them.

- [ ] pandas
- [ ] polars
- [ ] ibis
- [ ] modin
- [ ] duckdb
- [ ] dask
- [ ] vaex
- [ ] datatable
- [ ] pyarrow


## Concepts

Seperate in your mind "dataframe library" and "data format":

- Apache Arrow is a columnar in-memory data format. It is not a dataframe library
- dataframe libraries use whatever in-memory data format they prefer as their underlying data format (e.g. polars, duckdb, vaex, pyarrow).
