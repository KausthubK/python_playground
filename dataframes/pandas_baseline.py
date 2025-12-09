import pandas as pd

def filter_for_last_name(last_name: str, df: pd.DataFrame) -> pd.DataFrame:
    return df[df.last_name == last_name]

def filter_for_first_name(first_name: str, df: pd.DataFrame) -> pd.DataFrame:
    return df[df.first_name == first_name]

def count_by_state(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate counts per state."""
    return df.groupby('state').size().reset_index(name='count')

def count_by_first_name(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate counts per first name."""
    return df.groupby('first_name').size().reset_index(name='count')

def count_by_email_provider(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate counts per email provider (domain)."""
    df_copy = df.copy()
    df_copy['email_provider'] = df_copy['email'].str.split('@').str[1]
    return df_copy.groupby('email_provider').size().reset_index(name='count')

