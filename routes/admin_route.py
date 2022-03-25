from flask import request, Blueprint, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import admin

adminRoute = Blueprint("adminRoute", __name__)


@adminRoute.before_request
def before_request_user():
    if "logged" in session:
        name = session["name"]
        g.username = name


@adminRoute.route("/admin/create", methods=["POST"])
def add_admin():
    if session["idAdmin"]:
        admin.Admin.name = request.form["name"]
        admin.Admin.password = request.form["password"]
        admin.Admin.idStaff = request.form["idStaff"]
        password_hash = generate_password_hash(admin.Admin.password)

        new_admin = admin.Admin(admin.Admin.name, password_hash, admin.Admin.idStaff)
        db.session.add(new_admin)
        db.session.commit()
        return admin.admin_schema.jsonify(new_admin)


@adminRoute.route("/admin/<int:idAdmin>")
def get_admin(idAdmin):
    returnable = admin.Admin.query.get_or_404(idAdmin)
    return admin.admin_schema.dump(returnable)


@adminRoute.route("/admin/delete", methods=["DELETE"])
def delete_admin():
    get_id = request.form["idAdmin"]
    admin.Admin.password = request.form["password"]
    checking_admin = (
        db.session.query(admin.Admin).filter(get_id == admin.Admin.idAdmin).first()
    )
    if check_password_hash(checking_admin.password, admin.Admin.password):
        returnable = admin.Admin.query.get_or_404(get_id)
        db.session.delete(returnable)
        db.session.commit()
    else:
        return "Password is wrong. Try again.", 400

    return "", 204


@adminRoute.route("/admin/edit", methods=["POST"])
def edit_admin():
    get_id = request.form["idAdmin"]
    get_password = request.form["password"]
    checking_admin = (
        db.session.query(admin.Admin).filter(get_id == admin.Admin.idAdmin).first()
    )
    if check_password_hash(checking_admin.password, get_password):
        returnable = admin.Admin.query.get_or_404(get_id)
        if "name" in request.form:
            returnable.name = request.form["name"]
        if "password_new" in request.form:
            new_password = request.form["password_new"]
            password_hash = generate_password_hash(new_password)
            returnable.password = password_hash
        if "idStaff" in request.form:
            returnable.idStaff = request.form["idStaff"]

        db.session.commit()
        return admin.admin_schema.dump(returnable), 200
    else:
        return "Password is wrong. Try again.", 400


@adminRoute.route("/login", methods=["GET", "POST"])
def login():
    if (
        request.method == "POST"
        and "name" in request.form
        and "password" in request.form
    ):
        name = request.form["name"]
        password = request.form["password"]
        account = db.session.query(admin.Admin).filter(name == admin.Admin.name).first()

        if account:
            if check_password_hash(account.password, password):
                session["logged"] = True
                session["idAdmin"] = account.idAdmin
                session["name"] = account.name
                return "Logged in", 200
            else:
                flash("Incorrect name or password. Try again.")
        else:
            return "All wrong", 400


@adminRoute.route("/logout")
def logout():
    session.pop("logged", None)
    session.pop("idAdmin", None)
    session.pop("name", None)
    return "logged off", 200
