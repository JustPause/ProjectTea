from datetime import datetime
from main import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Tea(db.Model):
    __tablename__ = 'tea'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    tea_group: Mapped[int] = mapped_column(nullable=False)  # 0 unlisted, 1 Black Tea, 2 Green Tea, 3 White Tea
    link: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)

class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    tea_id: Mapped[int] = mapped_column(ForeignKey('tea.id'), nullable=False)
    text: Mapped[str] = mapped_column(db.String(255), nullable=False)
    time: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    tea_id: Mapped[int] = mapped_column(ForeignKey('tea.id'), nullable=False)
    instructions: Mapped[str] = mapped_column(db.Text, nullable=False)