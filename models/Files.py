from sqlalchemy import ForeignKey

from app import db
from models.article import Article


class Files(db.Model):
    __tablename__ = 'files'
    idFile = db.Column(db.Integer, primary_key=True)
    idArticle = db.Column(ForeignKey(Article.idArticle), nullable=False)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
