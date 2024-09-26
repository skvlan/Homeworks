import sqlite3

def execute_query(query, args=()):
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        records = cursor.fetchall()
    return records




