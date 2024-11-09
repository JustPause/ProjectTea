from main import app, db
# from db.dataBaseConnection import Tea, Comment, Recipe

with app.app_context():
    db.create_all()
    print("Tables created successfully.")
    
    