import polars as pl

def filter_for_last_name(last_name: str, df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(pl.col('last_name') == last_name)

def filter_for_first_name(first_name: str, df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(pl.col('first_name') == first_name)

def count_by_state(df: pl.DataFrame) -> pl.DataFrame:
    """Aggregate counts per state."""
    return df.group_by('state').agg(pl.len().alias('count'))

def count_by_first_name(df: pl.DataFrame) -> pl.DataFrame:
    """Aggregate counts per first name."""
    return df.group_by('first_name').agg(pl.len().alias('count'))

def count_by_email_provider(df: pl.DataFrame) -> pl.DataFrame:
    """Aggregate counts per email provider (domain)."""
    return df.with_columns(
        pl.col('email').str.split('@').list.get(1).alias('email_provider')
    ).group_by('email_provider').agg(pl.len().alias('count'))
