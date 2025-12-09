import duckdb

def filter_for_last_name(last_name: str, df: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    return df.filter(f"last_name = '{last_name}'")

def filter_for_first_name(first_name: str, df: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    return df.filter(f"first_name = '{first_name}'")

def count_by_state(df: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    """Aggregate counts per state."""
    return df.aggregate("state, count(*) as count", "state")

def count_by_first_name(df: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    """Aggregate counts per first name."""
    return df.aggregate("first_name, count(*) as count", "first_name")

def count_by_email_provider(df: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    """Aggregate counts per email provider (domain)."""
    return df.aggregate("split_part(email, '@', 2) as email_provider, count(*) as count", "split_part(email, '@', 2)")
