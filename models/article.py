from sqlalchemy import DateTime, func

from app import db, ma


class Article(db.Model):
    __tablename__ = "article"
    idArticle = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(4294000), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    date = db.Column(DateTime(timezone=True), default=func.now())
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    mimetype = db.Column(db.Text, nullable=False)

    def __init__(self, title, body, author, categoria, filename, data, mimetype):
        self.title = title
        self.body = body
        self.author = author
        self.categoria = categoria
        self.filename = filename
        self.data = data
        self.mimetype = mimetype


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("title", "author", "date", "body", "categoria", "filename", "data", "mimetype")


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
