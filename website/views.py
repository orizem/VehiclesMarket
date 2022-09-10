# views.py

from flask import Blueprint, render_template
from .create_map import CreateMap
from flask_login import login_required, current_user
from .templatetags.test import search_filter
from django import template
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.ops import unary_union
from os.path import join
from .config import PROJECT_NAME

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
    _vehicles = pd.read_csv(join(PROJECT_NAME, r"test_files\car data.csv"))
    html = _vehicles.to_html(classes='table table-striped table-dark', table_id='data').replace('<thead', '<thead class="table-light"')
    return render_template('search.html', page='search', df=html)

@main.route('/analytics')
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
    gdf2.crs = gdf.crs 

    heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gdf2.geometry ]

    CreateMap([gdf, gdf2, heat_data], ['Polygon', 'Points', 'Heat Map'])
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
