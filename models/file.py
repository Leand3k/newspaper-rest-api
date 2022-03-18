from sqlalchemy import ForeignKey
from models.article import Article
from app import db, ma


class Files(db.Model):
    __tablename__ = 'files'
    idFile = db.Column(db.Integer, primary_key=True)
    idArticle = db.Column(ForeignKey(Article.idArticle), nullable=False)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

    def __init__(self, idArticle, filename, data):
        self.idArticle = idArticle
        self.filename = filename
        self.data = data


class FilesSchema(ma.Schema):
    class Meta:
        fields = ('idFile', 'idArticle', 'filename', 'data')


file_schema = FilesSchema()
files_schema = FilesSchema(many=True)
