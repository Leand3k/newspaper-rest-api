import json

from flask import request, jsonify, Blueprint, send_file
from werkzeug.utils import secure_filename

from models import file
from app import db

filesRoute = Blueprint('filesRoute', __name__)


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


jsonserialiaze = Object()


@filesRoute.route('/files', methods=['POST'])
def add_file():
    multimedia = request.files['multimedia']
    if not multimedia:
        return 'No picture uploaded', 400

    filename = secure_filename(multimedia.filename)
    file.Files.filename = filename
    mimetype = multimedia.mimetype
    file.Files.mimetype = mimetype
    file.Files.data = multimedia
    if not filename:
        return 'Bad Upload!!', 400

    data = file.Files(file.Files.filename, file.Files.data.read(), file.Files.mimetype)

    db.session.add(data)
    db.session.commit()

    return file.file_schema.jsonify(data)
