import sqlite3

def create_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE your_table_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            link TEXT NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute("INSERT INTO your_table_name (name, link) VALUES ('Tea', '/teaList')")
    cursor.execute("INSERT INTO your_table_name (name, link) VALUES ('Coffee', '/coffeeList')")
    cursor.execute("INSERT INTO your_table_name (name, link) VALUES ('Juice', '/juiceList')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
