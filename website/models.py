# models.py

from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    full_name = db.Column(db.String(1000))
    password = db.Column(db.String(100))