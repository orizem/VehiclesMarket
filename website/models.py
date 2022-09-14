# models.py

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    full_name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    # Profile attributes
    phone_number = db.Column(db.String(50))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    profession = db.Column(db.String(50))
    addition_details = db.Column(db.Text)
    img = db.Column(db.String(1000000), unique=True)
    img_name = db.Column(db.String(1000), unique=True)
