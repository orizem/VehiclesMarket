# This file handles all routes to pages like: profile, analytics
# profile - GET
# edit_profile - GET, POST
# search - GET
# analytics - GET

import geopandas as gpd
import base64
from . import db
from .models import User, Vehicle
from base64 import b64decode
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from django import template
from os.path import join
import numpy as np
from shapely.ops import unary_union
from .templatetags.test import search_filter
from .create_map import CreateMap
from .config import PROJECT_NAME
from .forms import ProfileForm, VehicleForm, SearchForm
from werkzeug.utils import secure_filename


views = Blueprint('views', __name__)


def page_not_found(e):
  return render_template('404.html'), 404


@views.route('/')
def index():
    return render_template('index.html', page='home')


@views.route('/profile')
@login_required
def profile():
    # Search for the user in database
    user = User.query.filter_by(id=current_user.id).first()
    profile_img = ''
    if user.img:
        profile_img = base64.b64encode(user.img).decode()  # Convert BLOB to binary 64
    
    # Search for the vehicles that the user has been uploaded into database
    vehicles = Vehicle.query.filter_by(user_id=user.id).all()
    if vehicles:
        # Convert all the vehicles images
        for vehicle in vehicles:
            vehicle_img = ''
            if vehicle.img:
                vehicle_img = vehicle.img
            vehicle.img = base64.standard_b64encode(vehicle_img).decode('utf-8')  # Convert BLOB to binary 64

    return render_template('profile.html', user=user, profile_img=profile_img, vehicles=vehicles)


@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileForm()
    user = User.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        # Update user's profile
        user.phone_number = form.phone_number.data
        user.state = form.state.data
        user.city = form.city.data
        user.gender = form.gender.data
        user.profession = form.profession.data
        user.addition_details = form.addition_details.data
        if not form.img.data:
            user.img = ''
            user.img_name = ''
        else:
            user.img = form.img.data.read()
            user.img_name = secure_filename(form.img.data.filename)
        db.session.commit()
        return redirect(url_for('views.profile'))

    return render_template('edit_profile.html', name='edit_profile', form=form, is_profile_exist=True)


@views.route('/delete_profile', methods=['GET', 'POST'])
@login_required
def delete_profile():
    # Search user in database
    user = User.query.filter_by(id=current_user.id).first()
    # Delete user profile
    user.phone_number = None
    user.state = None
    user.city = None
    user.gender = None
    user.profession = None
    user.addition_details = None
    user.img = None
    user.img_name = None
    db.session.commit()
    return redirect(url_for('views.profile'))


@views.route('/upload_vehicle', methods=['GET','POST'])
@login_required
def upload_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        uploaded_img = form.img.data
        if not uploaded_img:
            vehicle_img = ''
            vehicle_img_filename = ''
        else:
            vehicle_img = uploaded_img.read()
            vehicle_img_filename = secure_filename(form.img.data.filename)

        # Add a Vehicle
        vehicle_to_add = Vehicle(brand=form.brand.data, model=form.model.data, edition=form.edition.data, year=form.year.data, 
                                condition=form.condition.data, transmission=form.transsmission.data, body=form.body.data, 
                                fuel=form.fuel.data, capacity=form.capacity.data, img=vehicle_img, img_name=vehicle_img_filename, user_id=current_user.id)
        db.session.add(vehicle_to_add)
        db.session.commit()
        return redirect(url_for('views.profile'))

    return render_template('upload_vehicle.html', form=form)


@views.route('/delete_vehicle/<int:id>')
@login_required
def delete_vehicle(id):
    # Search for vehicle to delete from database
    vehicle_to_delete = Vehicle.query.filter_by(id=id).first()
    if vehicle_to_delete:
        db.session.delete(vehicle_to_delete)
        db.session.commit()
        return redirect(url_for('views.profile'))
    
    return render_template('profile.home')


@views.route('/search')
@login_required
def search():
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
