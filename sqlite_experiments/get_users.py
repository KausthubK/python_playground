import sqlite3
import pandas as pd


def get_users(
    connection: sqlite3.Connection,
) -> pd.DataFrame:
    cursor = connection.cursor()
  
    query = f"""
    select *
    from users
    """
    return pd.read_sql_query(sql=query, con=connection)

if __name__ == '__main__':
    connection = sqlite3.connect('./data.db')
    print(get_users(connection=connection))