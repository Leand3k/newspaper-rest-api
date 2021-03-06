from app import db, ma


class Files(db.Model):
    __tablename__ = "files"
    idFile = db.Column(db.Integer, primary_key=True)
    # idArticle = db.Column(ForeignKey(Article.idArticle), nullable=False)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    mimetype = db.Column(db.Text, nullable=False)

    def __init__(self, filename, data, mimetype):
        self.filename = filename
        self.data = data
        self.mimetype = mimetype


class FilesSchema(ma.Schema):
    class Meta:
        fields = ("filename", "mimetype")


file_schema = FilesSchema()
files_schema = FilesSchema(many=True)
