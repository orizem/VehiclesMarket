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
from .forms import ProfileForm
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

@views.route('/post_vehicle')
@login_required
def post_vehicle():
    from . import db
    from .forms import PostVehicleForm
    from .models import PostVehicle
    form_post_vehicle = PostVehicleForm()
    if form_post_vehicle.validate_on_submit():
        vehicle_to_add = PostVehicle(
            img = form_post_vehicle.img.data, 
            brand = form_post_vehicle.brand.data,
            model = form_post_vehicle.model.data,
            edition = form_post_vehicle.edition.data,
            year = form_post_vehicle.year.data,
            condition = form_post_vehicle.condition.data,
            transmission = form_post_vehicle.transmission.data,
            body = form_post_vehicle.body.data,
            fuel = form_post_vehicle.fuel.data,
            capacity = form_post_vehicle.capacity.data
        )
        db.session.add(vehicle_to_add)
        db.session.commit()
    return render_template('post_vehicle.html', page='post_vehicle', form=form_post_vehicle)


register = template.Library()

def search_filter(df=None, col=0):
    # return 'search filter is working'
    df = df.sort_values(by=[df.columns[col]])
    return df
    # return render_template('search.html', name=current_user.name, page='search', vehicles=df)
