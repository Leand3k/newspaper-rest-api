
from flask import request, jsonify, Blueprint
from models import file
from app import db

filesRoute = Blueprint('filesRoute', __name__)


@filesRoute.route('/files', methods=['POST'])
def add_file():
    file.Files.idArticle = request.json['idArticle']
    file.Files.filename = request.json['filename']
    file.Files.data = request.files['data']

    new_file = file.Files(file.Files.idArticle, file.Files.filename, file.Files.data)
    db.session.add(new_file)
    db.session.commit()

    return file.file_schema.jsonify(new_file)
