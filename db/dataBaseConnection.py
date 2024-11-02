from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Tea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    link = db.Column(db.String(200), unique=True, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey('tea.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey('tea.id'), nullable=False)
    instructions = db.Column(db.Text, nullable=False)  