from flask import Flask, send_from_directory, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from getDataFormJson import teaList as teaListMethod 
from config import Config

app = Flask(__name__, static_folder = 'Front-End/dist', static_url_path = '')
app.config.from_object(Config)
db = SQLAlchemy(app)

categorys=["Green-Teas", "White-Teas", "Black-Teas"]
teaList = teaListMethod()[:3]
tea_names=[]

for subList in teaList:
    for tea in subList:
        tea_names.append(tea['name'])

from dataBaseConnection import Tea, Comment, Recipe

from working_with_data import insert_data, get_search_data, get_comments, insert_comment, get_random_comment, update_comment_with_tea_id,delete_comment_with_id

with app.app_context():
    db.create_all()
    insert_data()

@app.route('/api/initial-data', methods=['GET'])
def initial_data():
    return jsonify(get_search_data())

@app.route('/api/get_comments', methods=['POST'])
def comments():
    return jsonify(get_comments(request.get_json().get('teaName')))

@app.route('/api/get_comment', methods=['GET'])
def get_comment():
    return jsonify(get_random_comment())

@app.route("/")
def index():
    return send_from_directory('Front-End/dist', 'index.html')
  
@app.route("/benefits")
def benefits():
    return send_from_directory('Front-End/dist', 'benefits/index.html')
  
@app.route("/profile", methods=["GET", "POST"])
def profile():
    
    if request.method == "POST":

        form_type = request.form.get("form_type")
        
        if form_type == "Comment":
            comment_id = request.form.get("comment_id")
            comment = request.form.get("comment")
            update_comment_with_tea_id(comment_id, comment)
            
        elif form_type == "Delete":
            comment_id = request.form.get("comment_id")
            print("Deleting comment ", comment_id)
            delete_comment_with_id(comment_id)
    
    return send_from_directory('Front-End/dist', 'profile/index.html')
  
@app.route("/recipes")
def recipes():
    return send_from_directory('Front-End/dist', 'recipes/index.html')
  
# @app.route("/singleTea")
# def singleTea():
#     return send_from_directory('Front-End/dist', 'singleTea.html')
  
@app.route("/teaList")
def teaList():
    return send_from_directory('Front-End/dist', 'teaList/index.html')
  
@app.route("/team")
def team():
    return send_from_directory('Front-End/dist', 'team/index.html')

@app.route('/tea/<category>/<tea_name>', methods=["GET", "POST"])
def to_tea(category, tea_name):
    
    if request.method == "POST":
        
        comment = request.form.get("comment")
        # print(tea_name," : ", comment)
        insert_comment(tea_name,comment)
        
        return send_from_directory('Front-End/dist', f"tea/{category}/{tea_name}/index.html")
    
    if tea_name in tea_names:
        
        return send_from_directory('Front-End/dist', f"tea/{category}/{tea_name}/index.html")
    
    else:
        
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
  return send_from_directory('Front-End/dist', '404.html'), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)