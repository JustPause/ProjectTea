from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
app = Flask(__name__, static_folder='Front-End/dist', static_url_path='')

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ProjectTea.db"
db.init_app(app)

@app.route("/")
def index():
    return send_from_directory('Front-End/dist', 'index.html')
  
@app.route("/benefits")
def benefits():
    return send_from_directory('Front-End/dist', 'benefits/index.html')
  
@app.route("/profile")
def profile():
    return send_from_directory('Front-End/dist', 'profile.html')
  
@app.route("/recipes")
def recipes():
    return send_from_directory('Front-End/dist', 'recipes.html')
  
@app.route("/singleTea")
def singleTea():
    return send_from_directory('Front-End/dist', 'singleTea.html')
  
@app.route("/teaList")
def teaList():
    return send_from_directory('Front-End/dist', 'teaList.html')
  
@app.route("/team")
def team():
    return send_from_directory('Front-End/dist', 'team.html')

@app.errorhandler(404)
def page_not_found(e):
  return send_from_directory('Front-End/dist', '404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)