# This file handles all routes to pages like: profile, analytics
# profile - GET, POST
# search - GET
# analytics - GET

from base64 import b64decode
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from django import template
from os.path import join
import numpy as np
from shapely.ops import unary_union
import geopandas as gpd
from .templatetags.test import search_filter
from .create_map import CreateMap
from .config import PROJECT_NAME
from .forms import ProfileForm,SearchForm
from werkzeug.utils import secure_filename
import base64

views = Blueprint('views', __name__)

def page_not_found(e):
  return render_template('404.html'), 404

@views.route('/')
def index():
    return render_template('index.html', page='home')

@views.route('/profile')
@login_required
def profile():
    from .models import User
    from . import db

    user = User.query.filter_by(id=current_user.id).first()
    profile_is_exist = False
    if user.phone_number or user.state or user.city or user.gender or user.profession or user.addition_details:
        profile_is_exist = True
    img=''
    if user.img:
        # Convert BLOB to binary 64
        img = base64.b64encode(user.img).decode()
    # print(user.img)
    return render_template('profile.html', profile_is_exist=profile_is_exist, user=user, page='profile', img=img)

@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    from .models import User
    from . import db

    form = ProfileForm()
    user = User.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        user.phone_number = form.phone_number.data
        user.state = form.state.data
        user.city = form.city.data
        user.gender = form.gender.data
        user.profession = form.profession.data
        user.addition_details = form.addition_details.data
        user.phone_number = form.phone_number.data
        if not form.img.data:
            user.img_name = ''
        else:
            user.img = form.img.data.read()
            user.img_name = secure_filename(form.img.data.filename)
        db.session.commit()
        return redirect(url_for('views.profile'))
    return render_template('edit_profile.html', name='edit_profile', form=form)

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    from .models import Vehicle
    from . import db
    s_f = SearchForm()
    if s_f.validate_on_submit():
        res = Vehicle.query.filter(Vehicle.brand == s_f.brand.data,
        Vehicle.model == s_f.model.data,
        Vehicle.year >= s_f.from_year.data,Vehicle.year <= s_f.untill_year.data, # range of years
        Vehicle.price <= s_f.price.data,
        Vehicle.condition == s_f.condition.data,
        Vehicle.transmission == s_f.transmission.data,
        Vehicle.km_driven <= s_f.km_driven.data,
        Vehicle.fuel == s_f.fuel.data,
        Vehicle.capacity == s_f.capacity.data).all()
        headers = ("brand", "model", "year","price", "condition", "transmission","km driven", "fuel", "capacity")
        return render_template('search.html', page='search', form=s_f, data=res, search_headers=headers)
    else:
        return render_template('search.html', page='search',form=s_f)

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
