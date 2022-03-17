import os
from datetime import timedelta
from flask import Flask, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_migrate import Migrate


DATABASE_URL = os.getenv("DATABASE_URL")
app = Flask(__name__)



app.secret_key = "secret key owo"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bssyuskspjibud:de2dd9081d0f0dcde4681a044ac37fda807b671e0467d9f1ee7f30977b4a419a@ec2-3-216-221-31.compute-1.amazonaws.com:5432/da64e5emrdj031"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)
from models import admin, article, Files
db.drop_all()
db.create_all()
migrate = Migrate(app, db)




@app.route("/")
def hello():
    return {"Hello", "world"}


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
