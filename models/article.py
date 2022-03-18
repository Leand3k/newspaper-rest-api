from sqlalchemy import ForeignKey

from app import db, ma


class Article(db.Model):
    __tablename__ = 'article'
    idArticle = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, title, body, author, date):
        self.title = title
        self.body = body
        self.author = author
        self.date = date


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'author', 'date')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
