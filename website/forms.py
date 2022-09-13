from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, FileField
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
    
# Post vehicle Flask form
class PostVehicleForm(FlaskForm):
    img = FileField('img')
    brand = StringField('brand', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    model = StringField('model', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    edition = StringField('edition', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    year = StringField('year', validators=[Length(4)], render_kw={'style':'width:30%; margin:0 auto;'})
    condition = StringField('condition', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    transmission = StringField('transmission', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    body = StringField('body', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    fuel = StringField('fuel', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    capacity = StringField('capacity', validators=[Length(1, 20)], render_kw={'style':'width:30%; margin:0 auto;'})
    submit = SubmitField('Post')