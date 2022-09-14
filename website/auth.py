# This file handles the operations: Login, Logout and Signup

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .forms import LoginForm, SignupForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data): 
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('views.profile')
            # Add success message
        login_user(user, remember=form.remember_me.data)
        return redirect(next)
    return render_template('login.html', page='login', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm()
    # Check if POST request
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        # Validation process
        if user: # if a user is found, we want to redirect back to signup page so user can try again  
            flash('Email address already exists')
        elif form.password1.data != form.password2.data:
            flash('Passwords dont match')
        # Add user to database
        else:
            user_to_add = User(email=form.email.data, full_name=form.full_name.data, password=generate_password_hash(form.password1.data, 'sha256'))
            db.session.add(user_to_add)
            db.session.commit()
            login_user(user_to_add, remember=True)
            return redirect(url_for('views.profile'))
    return render_template('signup.html', page='signup', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))