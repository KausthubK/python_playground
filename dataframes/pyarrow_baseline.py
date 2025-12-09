import pyarrow as pa
import pyarrow.compute as pc

def filter_for_last_name(last_name: str, df: pa.Table) -> pa.Table:
    mask = pc.equal(df['last_name'], last_name)
    return df.filter(mask)

def filter_for_first_name(first_name: str, df: pa.Table) -> pa.Table:
    mask = pc.equal(df['first_name'], first_name)
    return df.filter(mask)

def count_by_state(df: pa.Table) -> pa.Table:
    """Aggregate counts per state."""
    grouped = df.group_by('state').aggregate([('state', 'count')])
    return grouped.rename_columns(['state', 'count'])

def count_by_first_name(df: pa.Table) -> pa.Table:
    """Aggregate counts per first name."""
    grouped = df.group_by('first_name').aggregate([('first_name', 'count')])
    return grouped.rename_columns(['first_name', 'count'])

def count_by_email_provider(df: pa.Table) -> pa.Table:
    """Aggregate counts per email provider (domain)."""
    # Extract email provider from email column
    email_split = pc.split_pattern(df['email'], '@')
    email_provider = pc.list_element(email_split, 1)

    # Add email_provider column
    df_with_provider = df.append_column('email_provider', email_provider)

    # Group by email_provider
    grouped = df_with_provider.group_by('email_provider').aggregate([('email_provider', 'count')])
    return grouped.rename_columns(['email_provider', 'count'])
