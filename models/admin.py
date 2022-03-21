from sqlalchemy import ForeignKey

from app import db, ma


class Admin(db.Model):
    __tablename__ = "Admin"
    idAdmin = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text, nullable=False)
    idStaff = db.Column(db.Integer, nullable=False)

    def __init__(self, name, password, idStaff):
        self.name = name
        self.password = password
        self.idStaff = idStaff


class AdminSchema(ma.Schema):
    class Meta:
        fields = ("idAdmin", "name", "password", "idStaff")


admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)
