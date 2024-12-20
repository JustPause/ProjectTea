from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from main import db

class Tea(db.Model):
    __tablename__ = 'tea'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), nullable=False)
    tea_group: Mapped[str] = mapped_column(nullable=False)  # 1 Black Tea, 2 Green Tea, 3 White Tea
    link: Mapped[str] = mapped_column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<Tea {self.name}>'

class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    tea_id: Mapped[int] = mapped_column(ForeignKey('tea.id'), nullable=False)
    text: Mapped[str] = mapped_column(db.String(2047), nullable=False)
    userName: Mapped[str] = mapped_column(db.String(255), nullable=False)
    location: Mapped[str] = mapped_column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Comment {self.tea_id}>'
    
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    tea_id: Mapped[int] = mapped_column(ForeignKey('tea.id'), nullable=False)
    instructions: Mapped[str] = mapped_column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Recipe {self.id}>'