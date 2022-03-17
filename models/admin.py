from sqlalchemy import ForeignKey

from app import db



class Admin(db.Model):
    __tablename__ = 'Admin'
    idAdmin = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text, nullable=False)
    idStaff = db.Column(db.Integer, nullable=False)
