# This file is for Flask Forms: Login, SignUp, Profile, Vehicle

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import Email, Length, DataRequired
from .config import CITIES_DICT


# Sign-up form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


# Sign-up form
class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 100), Email()])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1, 20)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(4, 50)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), Length(4, 50)])
    submit = SubmitField('Sign up')


# Profile form
class ProfileForm(FlaskForm):
    phone_number = StringField('Phone Number')
    state = StringField('State')
    city = SelectField('City', choices=[(x['city'], x['city']) for x in CITIES_DICT])
    gender = SelectField('Gender', choices=[('male', 'male'), ('female', 'female'), ('other', 'other')])
    img = FileField('Upload an image')
    submit = SubmitField('Submit')


# Vehicle form
class VehicleForm(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    condition = SelectField('Condition', choices=[('excellent', 'Excellent'), ('good', 'Good'), ('normal', 'Normal'), ('bad', 'Bad')])
    transmission = SelectField('Transmission', choices=[('automatic', 'Automatic'), ('mannual', 'Mannual')])
    km_driven = StringField('km Driven')
    fuel = StringField('Fuel')
    capacity = StringField('Capacity')
    img = FileField('Upload an image')
    submit = SubmitField('Submit')


# Search Vehicle form
class SearchForm(FlaskForm):
    brand = StringField('Brand')
    model = StringField('Model')
    condition = SelectField(u'Condition', choices = ("","excellent","good","normal","bad"), default = "")
    transmission = SelectField(u'Transmission', choices = ("","automatic","mannual"), default = "")
    fuel = StringField('Fuel')
    search = SubmitField('Search')
    download = SubmitField('CSV')
