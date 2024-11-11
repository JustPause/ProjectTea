import logging
from datetime import datetime
from dataBaseConnection import Tea, Comment, Recipe
from main import db
from sqlalchemy import MetaData, Table

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    @staticmethod
    def get_all_teas():
        query = 'SELECT * FROM tea'
        logger.info(f"Retrieved all teas: {len(query)} teas found.")
        return db.session.query(Tea).all()

    @staticmethod
    def get_comments_for_tea(tea_id):
        query = "SELECT * FROM comment WHERE tea_id = :tea_id"
        logger.info(f"Retrieved {len(query)} comments for tea_id {tea_id}.")
        return db.session.query(Comment).filter(Comment.tea_id == tea_id).all()

    @staticmethod
    def get_recipe_for_tea(tea_id):
        query = "SELECT * FROM recipe WHERE tea_id = :tea_id"
        logger.info(f"Retrieved recipe for tea_id {tea_id}.")
        return db.session.query(Recipe).filter(Recipe.tea_id == tea_id).first()

    @staticmethod
    def add_tea(name, tea_group, link):
        query = "INSERT INTO tea (name, tea_group, link) VALUES (:name, :tea_group, :link)"
        new_tea = Tea(name=name, tea_group=tea_group, link=link)
        db.session.add(new_tea)
        db.session.commit()
        logger.info(f"Added new tea: {name} (Group: {tea_group}, Link: {link})")
        return new_tea

    @staticmethod
    def add_comment(tea_id, text):
        query = "INSERT INTO comment (tea_id, text, time) VALUES (:tea_id, :text, :time)"
        new_comment = Comment(tea_id=tea_id, text=text, time=datetime.utcnow())
        db.session.add(new_comment)
        db.session.commit()
        logger.info(f"Added new comment for tea_id {tea_id}: {text}")
        return new_comment

    @staticmethod
    def add_recipe(tea_id, instructions):
        query = "INSERT INTO recipe (tea_id, instructions) VALUES (:tea_id, :instructions)"
        new_recipe = Recipe(tea_id=tea_id, instructions=instructions)
        db.session.add(new_recipe)
        db.session.commit()
        logger.info(f"Added new recipe for tea_id {tea_id}. Instructions: {instructions}")
        return new_recipe 
    
    @staticmethod
    def drop_tea_table():
        with db.engine.connect() as connection:
            tea_table = Table('tea', MetaData(), autoload_with=db.engine)
            tea_table.drop(connection)
            logger.info("Dropped 'tea' table.")
            
    @staticmethod
    def drop_comment_table():
        with db.engine.connect() as connection:
            comment_table = Table('comment', MetaData(), autoload_with=db.engine)
            comment_table.drop(connection)
            logger.info("Dropped 'comment' table.")
            
    @staticmethod
    def drop_recipe_table():
        with db.engine.connect() as connection:
            recipe_table = Table('recipe', MetaData(), autoload_with=db.engine)
            recipe_table.drop(connection)
            logger.info("Dropped 'recipe' table.")


    @staticmethod
    def close():
        db.session.close()
        
        