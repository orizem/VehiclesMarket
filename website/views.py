# views.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from django import template

from os.path import join
import numpy as np
import pandas as pd
from shapely.ops import unary_union
import geopandas as gpd

from .templatetags.test import search_filter
from .create_map import CreateMap
from .config import PROJECT_NAME

views = Blueprint('views', __name__)

def page_not_found(e):
  return render_template('404.html'), 404

@views.route('/')
def index():
    return render_template('index.html', page='home')

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, page='profile')

@views.route('/search')
@login_required
def search():
    from .forms import SearchForm
    search_form = SearchForm()
    return render_template('search.html', page='search', form=search_form)

@views.route('/analytics')
def analytics():
    gdf = gpd.read_file(join(PROJECT_NAME, r"shape files\israel.shp"))
    
    # find the bounds of your geodataframe
    x_min, y_min, x_max, y_max = gdf.total_bounds

    # set sample size
    n = 100
    # generate random data within the bounds
    x = np.random.uniform(x_min, x_max, n)
    y = np.random.uniform(y_min, y_max, n)

    # convert them to a points GeoSeries
    gdf_points = gpd.GeoSeries(gpd.points_from_xy(x, y))
    # only keep those points within polygons
    gdf_points = gdf_points[gdf_points.within(gdf.unary_union)]

    gdf2 = gpd.GeoDataFrame()
    gdf2['geometry'] = gdf_points
    gdf2['test'] = 'test'
    gdf2['x'] = gdf2['geometry'].x
    gdf2['y'] = gdf2['geometry'].y
    gdf2.crs = gdf.crs 

    heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gdf2.geometry ]

    CreateMap([gdf, gdf2, heat_data], ['Polygon', 'Points', 'Heat Map'])
    return render_template('analytics.html', page='analytics')

@views.route('/map')
def map():
    return render_template('map.html', page='analytics')


register = template.Library()

def search_filter(df=None, col=0):
    # return 'search filter is working'
    df = df.sort_values(by=[df.columns[col]])
    return df
    # return render_template('search.html', name=current_user.name, page='search', vehicles=df)
