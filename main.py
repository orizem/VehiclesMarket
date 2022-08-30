# main.py

from flask import Blueprint, render_template
from create_map import CreateMap
from flask_login import login_required, current_user
from templatetags.test import search_filter
from django import template

import pandas as pd

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
    _vehicles = pd.read_csv(r"test_files\car data.csv")
    return render_template('search.html', page='search', vehicles=_vehicles)

@main.route('/analytics')
def analytics():
    CreateMap()
    return render_template('analytics.html', page='analytics')

@main.route('/map')
def map():
    return render_template('map.html', page='analytics')


register = template.Library()

def search_filter(df=None, col=0):
    # return 'search filter is working'
    df = df.sort_values(by=[df.columns[col]])
    return df
    # return render_template('search.html', name=current_user.name, page='search', vehicles=df)
