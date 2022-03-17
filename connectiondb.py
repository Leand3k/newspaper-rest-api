from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import scoped_session, sessionmaker

from flask_migrate import Migrate
#
#
# app.secret_key = "secret key owo"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bssyuskspjibud" \
#                                         ":de2dd9081d0f0dcde4681a044ac37fda807b671e0467d9f1ee7f30977b4a419a@ec2-3-216" \
#                                         "-221-31.compute-1.amazonaws.com:5432/da64e5emrdj031 "
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# app.permanent_session_lifetime = timedelta(minutes=5)
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)