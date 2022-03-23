from flask import request, jsonify, Blueprint, send_file, Response
from werkzeug.utils import secure_filename
from models import file
from app import db
from models.file import Files

filesRoute = Blueprint("filesRoute", __name__)


@filesRoute.route("/files", methods=["POST"])
def add_file():
    multimedia = request.files["multimedia"]
    if not multimedia:
        return "No picture uploaded", 400

    filename = secure_filename(multimedia.filename)
    file.Files.filename = filename
    mimetype = multimedia.mimetype
    file.Files.mimetype = mimetype
    file.Files.data = multimedia
    if not filename:
        return "Bad Upload!!", 400

    data = file.Files(file.Files.filename, file.Files.data.read(), file.Files.mimetype)

    db.session.add(data)
    db.session.commit()

    return file.file_schema.jsonify(data)


@filesRoute.route("/files/<int:idFile>")
def get_file(idFile):

    returnable = db.session.query(Files).get(idFile)
    db.session.commit()

    if not returnable:
        return "Img not found", 404

    return Response(returnable.data, mimetype=returnable.mimetype)


@filesRoute.route("/files/delete/<int:idFile>")
def delete_file(idFile):
    returnable = db.session.query(Files).get(idFile)
    db.session.delete(returnable)
    db.session.commit()
    if not returnable:
        return "Img can not be deleted.", 404
    return "Img deleted", 200
