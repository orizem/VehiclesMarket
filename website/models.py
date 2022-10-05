# models.py

from time import timezone
from sqlalchemy.sql import func
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(50), unique=True)
    full_name = db.Column(db.String(20))
    password = db.Column(db.String(100))
    # Profile attributes
    phone_number = db.Column(db.String(15))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    profession = db.Column(db.String(50))
    addition_details = db.Column(db.Text)
    img = db.Column(db.String(500))
    img_name = db.Column(db.String(500))
    vehicles = db.relationship('Vehicle') # One to many

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    brand = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.String(4))
    price = db.Column(db.Integer)
    condition = db.Column(db.String(20))
    transmission = db.Column(db.String(20))
    km_driven = db.Column(db.Integer)
    fuel = db.Column(db.String(20))
    capacity = db.Column(db.Integer)
    img = db.Column(db.String(500))
    img_name = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
