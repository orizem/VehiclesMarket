# This file handles the routes of: 
# 1) Profile - User and Vehicles.
    # The operations enabled are: create or edit or delete a profile, upload or delete a vehicle.
# 2) Analytics - Responsive Heatmap. 
    # There are 3 layers one on top of another:
    # 1. Polygon of Israel state in blue
    # 2. Heat Map
    # 3. Points - each points is a vehicle (specified by the city of the user)
# 3) Search - Search box to find the owner of the Vehicle (with contact details)

import csv
from io import StringIO
import pandas as pd
import geopandas as gpd
import base64
from . import db
from .models import User, Vehicle
from base64 import b64decode
from flask import Blueprint, Response, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from os.path import join
import numpy as np
from shapely.ops import unary_union
from .create_map import CreateMap
from .config import PROJECT_NAME, CITIES_DICT
from .forms import ProfileForm, VehicleForm, SearchForm
from werkzeug.utils import secure_filename
import math


views = Blueprint('views', __name__)


def page_not_found(e):
  return render_template('404.html'), 404


@views.route('/')
def index():
    return render_template('README.html', page='home')


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

    return render_template('profile.html', user=user, page='profile', profile_img=profile_img, vehicles=vehicles)


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
        if not form.img.data:
            user.img = ''
            user.img_name = ''
        else:
            user.img = form.img.data.read()
            user.img_name = secure_filename(form.img.data.filename)
        db.session.commit()
        return redirect(url_for('views.profile'))
    
    # Update values of the form
    form.phone_number.data = user.phone_number
    form.state.data = user.state
    form.city.data = user.city
    form.gender.data = user.gender

    return render_template('edit_profile.html', user=current_user, form=form, page='edit_profile')


@views.route('/delete_profile', methods=['GET', 'POST'])
@login_required
def delete_profile():
    # Search user in database
    user = User.query.filter_by(id=current_user.id).first()
    # Delete user profile
    user.phone_number = ''
    user.state = ''
    user.city = ''
    user.gender = ''
    user.img = ''
    user.img_name = ''
    db.session.commit()
    return redirect(url_for('views.profile'))


@views.route('/upload_vehicle', methods=['GET','POST'])
@login_required
def upload_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        uploaded_img = form.img.data
        # Add a Vehicle
        vehicle_to_add = Vehicle(brand=form.brand.data, model=form.model.data, year=form.year.data, price=form.price.data, 
                                condition=form.condition.data, transmission=form.transmission.data, km_driven=form.km_driven.data, 
                                fuel=form.fuel.data, capacity=form.capacity.data, img=uploaded_img.read(), img_name=secure_filename(uploaded_img.filename), 
                                user_id=current_user.id)
        db.session.add(vehicle_to_add)
        db.session.commit()
        return redirect(url_for('views.profile'))

    return render_template('upload_vehicle.html', form=form, page='upload_vehicle')


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


@views.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    vehicles = Vehicle.query.all()
    
    sort_model = None

    # Returns the requested model to order by it
    def get_model(model_name):
        if model_name == 'brand':
            return Vehicle.brand
        elif model_name == 'model':
            return Vehicle.model
        elif model_name == 'year':
            return Vehicle.year
        elif model_name == 'price':
            return Vehicle.price
        elif model_name == 'condition':
            return Vehicle.condition
        elif model_name == 'transmission':
            return Vehicle.transmission
        elif model_name == 'km_driven':
            return Vehicle.km_driven
        elif model_name == 'fuel':
            return Vehicle.fuel
        elif model_name == 'capacity':
            return Vehicle.capacity

    if search_form.sort_by.data:
        sort_model = get_model(search_form.sort_by.data)

    # Create csv file of the given table by the search parameters
    def generate_csv(vehicles_):
        data = StringIO()
        w = csv.writer(data)

        # write header
        w.writerow(('link','brand','model','year','price','condition','transmission','km_driven','fuel','capacity'))
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        # Write each row to the csv file
        for vehicle in vehicles_:
            w.writerow((f'http://localhost:5000/search/{vehicle.id}', vehicle.brand, vehicle.model, vehicle.year, vehicle.price,
             vehicle.condition, vehicle.transmission, vehicle.km_driven, vehicle.fuel, vehicle.capacity))
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    # Returs list of vehicles by the search parameters
    def get_vehicles():
        _vehicles = Vehicle.query.filter(Vehicle.brand.contains(search_form.brand.data),
            Vehicle.model.contains(search_form.model.data),
            # Vehicle.year >= int(search_form.from_year.data), Vehicle.year <= int(search_form.untill_year.data), # range of years
            Vehicle.price >= price_min_price,  Vehicle.price <= price_max_price, # range of prices
            Vehicle.condition.contains(search_form.condition.data),
            Vehicle.transmission.contains(search_form.transmission.data),
            Vehicle.km_driven >= km_min,  Vehicle.km_driven <= km_max, # range of km
            Vehicle.fuel.contains(search_form.fuel.data),
            Vehicle.capacity >= capacity_min,  Vehicle.capacity <= capacity_max, # range of capacities
            )
        # In case column to sort was selected, sort by this col
        if sort_model:
            if search_form.sort_type.data == 'ASC':
                return _vehicles.order_by(sort_model.asc()).all() 
            return _vehicles.order_by(sort_model.desc()).all()
        return _vehicles.all()

    # ========== Initializes ==========
    page_table, size_table = 0, 10
    price_min_price, price_max_price = 0, 9e5
    km_min, km_max = 0, 1e5
    capacity_min, capacity_max = 0, 3e3
    checkbox = "None"
    # ========== End of Initializes ==========

    if search_form.validate_on_submit():
        # Handle clear button pressed
        if search_form.clear.data:
            search_form.brand.data = None
            search_form.model.data = None
            search_form.condition.data = ""
            search_form.transmission.data = ""
            search_form.fuel.data = None
            search_form.table_size.data = "10"
            search_form.sort_by.data = ""
            search_form.sort_type.data = "ASC"
            checkbox = "None"
            return render_template('search.html', form=search_form, vehicles=vehicles, data=vehicles, page_table=page_table, size_table=size_table, checkbox=checkbox, page='search',
                slider_min_price=price_min_price, slider_max_price=price_max_price, slider_min_km=km_min, slider_max_km=km_max, slider_min_capacity=capacity_min, slider_max_capacity=capacity_max)

        # ========== Initializes for submit ==========
        price_min_price = min(int(request.form["fromSliderPrice"]), int(request.form["toSliderPrice"]))
        price_max_price = max(int(request.form["fromSliderPrice"]), int(request.form["toSliderPrice"]))

        km_min = min(int(request.form["fromSliderKm"]), int(request.form["toSliderKm"]))
        km_max = max(int(request.form["fromSliderKm"]), int(request.form["toSliderKm"]))
        
        capacity_min = min(int(request.form["fromSliderCapacity"]), int(request.form["toSliderCapacity"]))
        capacity_max = max(int(request.form["fromSliderCapacity"]), int(request.form["toSliderCapacity"]))

        checkbox = f"{request.form.get('csv_checkbox')}"

        res = get_vehicles()
        page_table = int(request.form["page"])
        size_table = int(search_form.table_size.data)
        page_table = page_table if page_table < math.ceil(len(res)/size_table)-1 else math.ceil(len(res)/size_table)-1
        page_table = (page_table >= 0)*page_table
        # ========== End of Initializes for submit ==========

        # Handle search button pressed
        if search_form.search.data:
            return render_template('search.html', form=search_form, vehicles=vehicles, data=res, page_table=page_table, size_table=size_table, checkbox=checkbox, page='search',
                slider_min_price=price_min_price, slider_max_price=price_max_price, slider_min_km=km_min, slider_max_km=km_max, slider_min_capacity=capacity_min, slider_max_capacity=capacity_max)

        # Handle download button pressed
        if search_form.download.data:
            if checkbox=="None":
                res = res[page_table*size_table:(page_table+1)*size_table]

            response = Response(generate_csv(res), mimetype='text/csv')
            response.headers.set("Content-Disposition", "attachment", filename="vehicles.csv")
            return response
        
        # Handle previous button pressed
        if search_form.prevBtn.data:
            if page_table > 0:
                page_table -= 1
            return render_template('search.html', form=search_form, vehicles=vehicles, data=res, page_table=page_table, size_table=size_table, checkbox=checkbox, page='search',
                slider_min_price=price_min_price, slider_max_price=price_max_price, slider_min_km=km_min, slider_max_km=km_max, slider_min_capacity=capacity_min, slider_max_capacity=capacity_max)

        # Handle next button pressed
        if search_form.nextBtn.data:
            if page_table < math.ceil(len(res)/size_table)-1:
                page_table += 1
            return render_template('search.html', form=search_form, vehicles=vehicles, data=res, page_table=page_table, size_table=size_table, checkbox=checkbox, page='search',
                slider_min_price=price_min_price, slider_max_price=price_max_price, slider_min_km=km_min, slider_max_km=km_max, slider_min_capacity=capacity_min, slider_max_capacity=capacity_max)

    return render_template('search.html', form=search_form, vehicles=vehicles, data=vehicles, page_table=page_table, size_table=size_table, checkbox=checkbox, page='search',
             slider_min_price=price_min_price, slider_max_price=price_max_price, slider_min_km=km_min, slider_max_km=km_max, slider_min_capacity=capacity_min, slider_max_capacity=capacity_max)


@views.route('/search/<int:id>')
def display_vehicle(id):
    # Search vehicle in database
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
        if vehicle.img:
            vehicle_img = base64.b64encode(vehicle.img).decode()  # Convert BLOB to binary 64
        else:
            vehicle_img = None
        # Search user in database
        user = User.query.filter_by(id=vehicle.user_id).first()
        return render_template('display_vehicle.html', vehicle=vehicle, vehicle_img=vehicle_img, user=user)

    return render_template('404.html')


@views.route('/analytics')
def analytics():
    gdf = gpd.read_file(join(PROJECT_NAME, r"shape files\israel.shp"))
       
    users = User.query.all()
    vehicles = Vehicle.query.all()
    
    users_df = gpd.GeoDataFrame([{'id':u.id, 'city':u.city} for u in users])
    vehicles_df = gpd.GeoDataFrame([{'id':v.id, 'brand':v.brand, 'model':v.model, 'year':v.year, 'price':v.price, 'condition':v.condition, 'transmission':v.transmission,
                                     'km_driven':v.km_driven, 'fuel':v.fuel, 'capacity':v.capacity, 'img':v.img, 'img_name':v.img_name, 'user_id':v.user_id} for v in vehicles])
    merge_df = pd.merge(vehicles_df, users_df, left_on='user_id', right_on='id', how='left')    # Merge vehicles with users inorder to have city in vehicle
    
    merge_df['lat'] = 0.0
    merge_df['lng'] = 0.0
    
    # Set Latitude and Longtitude by city
    for x in CITIES_DICT:
        merge_df.loc[merge_df['city'] == x['city'], 'lat'] = x['lat']
        merge_df.loc[merge_df['city'] == x['city'], 'lng'] = x['lng']

    # Spreading the points inside the city  
    merge_df['lat'] = merge_df['lat'] + np.random.uniform(-0.05, 0.05, len(merge_df))
    merge_df['lng'] = merge_df['lng'] + np.random.uniform(-0.1, 0.1, len(merge_df))
    
    # Modifies to get the final result
    merge_df = merge_df.drop(columns=['img','img_name','user_id','id_y'])
    merge_df.columns = ['id'] + list(merge_df.columns[1:])
    merge_df = gpd.GeoDataFrame(merge_df, geometry=gpd.points_from_xy(merge_df['lng'], merge_df['lat']))
    merge_df = merge_df[merge_df['geometry'].within(gdf.unary_union)]
    merge_df.crs = gdf.crs
    
    # Heat map data
    heat_data = [[point.xy[1][0], point.xy[0][0]] for point in merge_df.geometry]

    # Generating map by given layears
    CreateMap([gdf, heat_data, merge_df], ['Polygon', 'Heat Map', 'Points'])

    return render_template('analytics.html', page='analytics')


@views.route('/map')
def map():
    return render_template('map.html')
