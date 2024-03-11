import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = f"""
CREATE TABLE users (id int, username text, password text)
"""

cursor.execute(create_table)

release_list = [
    (1, 'jose', 'asdf'),
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz'),
]

if __name__ == '__main__':
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", release_list)
    connection.commit()
    connection.close() 