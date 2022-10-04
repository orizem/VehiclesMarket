# This file is for Flask Forms: Login, SignUp

from tkinter.ttk import Style
from turtle import width

# from traitlets import default
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, FileField, IntegerField
from wtforms.validators import Email, Length, DataRequired



# Sign-up Flask form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


# Sign-up Flask form
class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 100), Email()])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1, 20)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(4, 50)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), Length(4, 50)])
    submit = SubmitField('Sign up')

# Profile Flask form
class ProfileForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[Length(9, 15)])
    state = StringField('State')
    city = StringField('City')
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    profession = StringField('Profession')
    addition_details = TextAreaField('Addition Details')
    img = FileField('Upload an image')
    submit = SubmitField('Submit')

# Search Vehicle form
class SearchForm(FlaskForm):
    brand = StringField('Brand')
    model = StringField('Model')
    from_year = SelectField(u'From year', choices = range(2000,2023,1), default =2000)
    untill_year = SelectField(u'Untill year', choices = range(2023,2000,-1), default =2023)
    price = IntegerField('price (up to)')
    condition = SelectField(u'Condition', choices = ("excellent","good","normal","bad"), default = "excellent")
    transmission = SelectField(u'Transmission', choices = ("automatic","mannual"), default = "automatic")
    km_driven = IntegerField('Km driven',default = -1)
    fuel = SelectField(u'Fuel', choices = ("Petrol","Petrol 98","Diesel"), default = "Petrol")
    capacity = IntegerField('Capacity')
    submit = SubmitField('Submit')
    # img = db.Column(db.String(500))
    # img_name = db.Column(db.String(500))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))