# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd
from templatetags.test import search_filter
from django import template


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', page='home')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, page='profile')

@main.route('/search')
@login_required
def search():
    _vehicles = pd.read_csv(r"C:\Users\orize\Documents\MEGA\MEGAsync\Study\Computer Engineering\year c\צד שרת\final_project\car data.csv")
    return render_template('search.html', name=current_user.name, page='search', vehicles=_vehicles)


register = template.Library()

def search_filter(df=None, col=0):
    # return 'search filter is working'
    df = df.sort_values(by=[df.columns[col]])
    return df
    # return render_template('search.html', name=current_user.name, page='search', vehicles=df)
