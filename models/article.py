

from sqlalchemy import DateTime, func

from app import db, ma


class Article(db.Model):
    __tablename__ = "article"
    idArticle = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(4294000000), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(DateTime(timezone=True), default=func.now())

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("title", "author", "date", "body")


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
