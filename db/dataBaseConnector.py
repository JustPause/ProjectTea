import sqlite3

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM your_table_name').fetchall()  # Replace with your actual table name
    conn.close()
    return data