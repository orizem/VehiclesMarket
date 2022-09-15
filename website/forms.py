# This file is for Flask Forms: Login, SignUp

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, FileField
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
    phone_number = StringField('Phone Number', validators=[Length(10, 11)])
    state = StringField('State')
    city = StringField('City')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    profession = StringField('Profession')
    addition_details = TextAreaField('Addition Details')
    img = FileField('Upload an image')
    submit = SubmitField('Submit')

# Search Vehicle form
class SearchForm(FlaskForm):
    model = StringField('Model')
    submit = SubmitField('Search')
