import sqlite3
from datetime import datetime
from db.dataBaseConnector import Tea
from main import db

def get_db_connection():
    conn = sqlite3.connect('db/TeaBase.db')
    conn.row_factory = sqlite3.Row  # To get dictionary-like access to rows
    return conn

class Database:
    def __init__(self):
        self.conn = get_db_connection()

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def get_all_teas(self):
        query = 'SELECT * FROM tea'
        teas = self.conn.execute(query).fetchall()
        return teas

    def get_comments_for_tea(self, tea_id):
        query = 'SELECT * FROM comment WHERE tea_id = ?'
        comments = self.conn.execute(query, (tea_id,)).fetchall()
        return comments

    def get_recipe_for_tea(self, tea_id):
        query = 'SELECT * FROM recipe WHERE tea_id = ?'
        recipe = self.conn.execute(query, (tea_id,)).fetchone()
        return recipe

    def add_tea(self, name, tea_group, link):
        new_tea = Tea(name=name, tea_group=tea_group, link=link)  # Create a new Tea object
        db.session.add(new_tea)  # Add the new Tea object to the session
        db.session.commit()  # Commit the transaction to save it to the database


    def add_comment(self, tea_id, text):
        query = 'INSERT INTO comment (tea_id, text, time) VALUES (?, ?, ?)'
        self.conn.execute(query, (tea_id, text, datetime.utcnow()))
        self.conn.commit()

    def add_recipe(self, tea_id, instructions):
        query = 'INSERT INTO recipe (tea_id, instructions) VALUES (?, ?)'
        self.conn.execute(query, (tea_id, instructions))
        self.conn.commit()
        
    def close(self):
        self.conn.close()