import ibis
from ibis.expr.types import Table

def filter_for_last_name(last_name: str, df: Table) -> Table:
    return df.filter(df.last_name == last_name)

def filter_for_first_name(first_name: str, df: Table) -> Table:
    return df.filter(df.first_name == first_name)

def count_by_state(df: Table) -> Table:
    """Aggregate counts per state."""
    return df.group_by('state').agg(count=df.count())

def count_by_first_name(df: Table) -> Table:
    """Aggregate counts per first name."""
    return df.group_by('first_name').agg(count=df.count())

def count_by_email_provider(df: Table) -> Table:
    """Aggregate counts per email provider (domain)."""
    df_with_provider = df.mutate(email_provider=df.email.split('@')[1])
    return df_with_provider.group_by('email_provider').agg(count=ibis._.count())
