import os
from datetime import timedelta
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL").replace("://", "ql://", 1)
app = Flask(__name__)
# db config
app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

# connection and creation of tables
db = SQLAlchemy(app)
ma = Marshmallow(app)
# importing models that will be created
from models import admin, article, file

# db.drop_all()
db.create_all()

# importing routes for blueprint
from routes.files_route import filesRoute
from routes.articles_route import articleRoute
from routes.admin_route import adminRoute

app.register_blueprint(filesRoute)
app.register_blueprint(articleRoute)
app.register_blueprint(adminRoute)


@app.route("/")
def hello():
    return "<p>Hi</p>"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
