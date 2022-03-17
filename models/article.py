from sqlalchemy import ForeignKey

from app import db
from models.Files import Files




class Article(db.Model):
    __tablename__='article'
    idArticle = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)


