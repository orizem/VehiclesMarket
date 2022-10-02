# This file handles all routes to pages like: profile, analytics
# profile - GET
# edit_profile - GET, POST
# search - GET
# analytics - GET
CITIES_DICT = [
    {'city':'Jerusalem', 'lat':31.7833 , 'lng':35.2167},
    {'city':'Tel Aviv-Yafo', 'lat':32.08 , 'lng':34.78},
    {'city':'Haifa', 'lat':32.8 , 'lng':34.9833},
    {'city':'Rishon LeZiyyon', 'lat':31.9711 , 'lng':34.7894},
    {'city':'Petah Tiqwa', 'lat':32.0833 , 'lng':34.8833},
    {'city':'Ashdod', 'lat':31.7978 , 'lng':34.6503},
    {'city':'Netanya', 'lat':32.3328 , 'lng':34.86},
    {'city':'Beersheba', 'lat':31.2589 , 'lng':34.7978},
    {'city':'Bene Beraq', 'lat':32.0807 , 'lng':34.8338},
    {'city':'Holon', 'lat':32.0167 , 'lng':34.7667},
    {'city':'Ramat Gan', 'lat':32.07 , 'lng':34.8235},
    {'city':'Bat Yam', 'lat':32.0231 , 'lng':34.7503},
    {'city':'Ashqelon', 'lat':31.6658 , 'lng':34.5664},
    {'city':'Rehovot', 'lat':31.8914 , 'lng':34.8078},
    {'city':'Bet Shemesh', 'lat':31.7514 , 'lng':34.9886},
    {'city':'Kefar Sava', 'lat':32.1858 , 'lng':34.9077},
    {'city':'Herzliyya', 'lat':32.1556 , 'lng':34.8422},
    {'city':'Nazareth', 'lat':32.7021 , 'lng':35.2978},
    {'city':'Raananna', 'lat':32.1833 , 'lng':34.8667},
    {'city':'Ramla', 'lat':31.9275 , 'lng':34.8625},
    {'city':'Givatayim', 'lat':32.0697 , 'lng':34.8117},
    {'city':'Hod HaSharon', 'lat':32.15 , 'lng':34.8833},
    {'city':'Qiryat Ata', 'lat':32.8 , 'lng':35.1},
    {'city':'Rosh HaAyin', 'lat':32.0833 , 'lng':34.95},
    {'city':'Umm el Fahm', 'lat':32.5158 , 'lng':35.1525},
    {'city':'Nes Ziyyona', 'lat':31.9333 , 'lng':34.8},
    {'city':'Elad', 'lat':32.0523 , 'lng':34.9512},
    {'city':'Ramat HaSharon', 'lat':32.15 , 'lng':34.8333},
    {'city':'Karmiel', 'lat':32.9 , 'lng':35.2833},
    {'city':'Qiryat Ono', 'lat':32.0636 , 'lng':34.8553},
    {'city':'Ben Zakkay', 'lat':31.8833 , 'lng':34.7333},
    {'city':'Qiryat Bialik', 'lat':32.8331 , 'lng':35.0664},
    {'city':'Or Yehuda', 'lat':32.0333 , 'lng':34.85},
    {'city':'Shefaram', 'lat':32.8056 , 'lng':35.1694},
    {'city':'Yehud', 'lat':32.0333 , 'lng':34.8833},
    {'city':'Givat Shemuel', 'lat':32.0781 , 'lng':34.8489},
    {'city':'Gedera', 'lat':31.8139 , 'lng':34.7783},
    {'city':'Et Tira', 'lat':32.2328 , 'lng':34.9503},
    {'city':'Gan Yavne', 'lat':31.7886 , 'lng':34.7053},
    {'city':'Kafr Qasim', 'lat':32.1142 , 'lng':34.9772},
    {'city':'Qalansuwa', 'lat':32.285 , 'lng':34.9811},
    {'city':'Hadera', 'lat':32.45 , 'lng':34.9167},
    {'city':'Modiin Makkabbim Reut', 'lat':31.9339 , 'lng':34.9856},
    {'city':'Lod', 'lat':31.95 , 'lng':34.9},
    {'city':'Rahat', 'lat':31.3925 , 'lng':34.7544},
    {'city':'Nahariyya', 'lat':33.0036 , 'lng':35.0925},
    {'city':'Eilat', 'lat':29.55 , 'lng':34.95},
    {'city':'Eilat', 'lat':32.9261 , 'lng':35.0839},
    {'city':'Afula', 'lat':32.6078 , 'lng':35.2897},
    {'city':'Tiberias', 'lat':32.7897 , 'lng':35.5247},
    {'city':'Pardes Hanna Karkur', 'lat':32.4711 , 'lng':34.9675},
    {'city':'Et Taiyiba', 'lat':3.2667,  'lng':35},
    {'city':'Qiryat Mozqin', 'lat':32.8369 , 'lng':35.0775},
    {'city':'Qiryat Yam', 'lat':32.8331 , 'lng':35.0664},
    {'city':'Maalot Tarshiha', 'lat':33.0167 , 'lng':35.2708},
    {'city':'Zefat', 'lat':32.9658 , 'lng':35.4983},
    {'city':'Tamra', 'lat':32.8511 , 'lng':35.2071},
    {'city':'Dimona', 'lat':31.07 , 'lng':35.03},
    {'city':'Sakhnin', 'lat':32.8667 , 'lng':35.3},
    {'city':'Netivot', 'lat':31.4167 , 'lng':34.5833},
    {'city':'Ofaqim', 'lat':31.2833 , 'lng':34.6167},
    {'city':'Migdal HaEmeq', 'lat':32.6786 , 'lng':35.2444},
    {'city':'Nesher', 'lat':32.7711 , 'lng':35.0394},
    {'city':'Arad', 'lat':31.2603 , 'lng':35.2147},
    {'city':'Kefar Yona', 'lat':32.315 , 'lng':34.9328},
    {'city':'Tirat Karmel', 'lat':32.7667 , 'lng':34.9667},
    {'city':'Sederot', 'lat':31.5261 , 'lng':34.5939},
    {'city':'Qiryat Malakhi', 'lat':31.7333 , 'lng':34.75},
    {'city':'Qiryat Shemona', 'lat':33.2075 , 'lng':35.5697},
    {'city':'Yoqneam Illit', 'lat':32.6594 , 'lng':35.11},
    {'city':'Beer Yaaqov', 'lat':31.9436 , 'lng':34.8392},
    {'city':'Or Aqiva', 'lat':32.5 , 'lng':34.9167},
    {'city':'Bet Shean', 'lat':32.4961 , 'lng':35.4989},
    {'city':'Majdal Shams', 'lat':33.2692 , 'lng':35.7706},
    {'city':'Jisr ez Zarqa', 'lat':32.5379 , 'lng':34.9122},
    {'city':'Omer', 'lat':31.2683 , 'lng':34.8489},
    {'city':'Buqata', 'lat':33.2014 , 'lng':35.7797}
]

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
            if vehicle.img:
                vehicle.img = base64.b64encode(vehicle.img).decode()  # Convert BLOB to binary 64
            else:
                vehicle.img = None

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

    return render_template('edit_profile.html', name='edit_profile', form=form)


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
            vehicle_img = uploaded_img
            vehicle_img_filename = secure_filename(form.img.data.filename)

        # Add a Vehicle
        vehicle_to_add = Vehicle(brand=form.brand.data, model=form.model.data, year=form.year.data, price=form.price.data, 
                                condition=form.condition.data, transmission=form.transmission.data, km_driven=form.km_driven.data, 
                                fuel=form.fuel.data, capacity=form.capacity.data, img=uploaded_img.read(), img_name=vehicle_img_filename, user_id=current_user.id)
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
