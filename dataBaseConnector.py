from datetime import datetime
from dataBaseConnection import Tea, Comment, Recipe
from main import db

class Database:
    def get_all_teas():
        query = 'SELECT * FROM tea'
        return db.session.query(Tea).all()

    def get_comments_for_tea(tea_id):
        query = "SELECT * FROM comment WHERE tea_id = :tea_id"
        return db.session.query(Comment).filter(Comment.tea_id == tea_id).all()

    def get_recipe_for_tea(tea_id):
        query = "SELECT * FROM recipe WHERE tea_id = :tea_id"
        return db.session.query(Recipe).filter(Recipe.tea_id == tea_id).first()

    def add_tea(name, tea_group, link):
        query = "INSERT INTO tea (name, tea_group, link) VALUES (:name, :tea_group, :link)"
        new_tea = Tea(name=name, tea_group=tea_group, link=link)
        db.session.add(new_tea)
        db.session.commit()
        return new_tea

    def add_comment(tea_id, text):
        query = "INSERT INTO comment (tea_id, text, time) VALUES (:tea_id, :text, :time)"
        new_comment = Comment(tea_id=tea_id, text=text, time=datetime.utcnow())
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    def add_recipe(tea_id, instructions):
        query = "INSERT INTO recipe (tea_id, instructions) VALUES (:tea_id, :instructions)"
        new_recipe = Recipe(tea_id=tea_id, instructions=instructions)
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe 
        
    def close():
        db.session.close()