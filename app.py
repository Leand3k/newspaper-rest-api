import os
from datetime import timedelta
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from flask import Flask, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_migrate import Migrate
import psycopg2
from psycopg2 import *

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
app = Flask(__name__)
# db config
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

# connection and creation of tables
db = SQLAlchemy(app)
ma = Marshmallow(app)
from models import admin, article, file
db.drop_all()
db.create_all()
migrate = Migrate(app, db)


@app.route("/")
def hello():

    return "<p>Hi</p>"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
