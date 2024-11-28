from flask import Flask, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from getDataFormJson import teaList as teaListMethod 

db = SQLAlchemy() 
app = Flask(__name__, static_folder='Front-End/dist', static_url_path='')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ProjectTea.db"
db.init_app(app)

tea_names = [tea['name'] for tea in teaListMethod()[0]]

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
    return send_from_directory('Front-End/dist', 'teaList/index.html')
  
@app.route("/team")
def team():
    return send_from_directory('Front-End/dist', 'team.html')

@app.route('/tea/green-tea/<tea_name>')
def redirect_to_tea(tea_name):
    if tea_name in tea_names:
        return send_from_directory('Front-End/dist', f"tea/green-tea/{tea_name}/index.html")
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
  return send_from_directory('Front-End/dist', '404.html'), 404

def setup():
    with app.app_context():
        db.create_all()

# setup()

if __name__ == "__main__":
    app.run(debug=True)