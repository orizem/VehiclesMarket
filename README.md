# VehiclesMarket
Full Stack web application

# Requirements
## Purpose
Visualize the vehicles on responsive Heat Map. New user can upload his vehicles and they would be added to the Heat Map or just view and search vehicles.
The Heat Map allows you to find out which areas have the most vehicles (red = many, green = less). The Heat map is available for all users, but to search vehilces manually, registration is required.
## Features - must
1) Responsive Heat Map - 3 layers one on top of another (Polygon of Israel state, Heat map, Points of existing vehicles).
2) Create and edit personal profile.
3) Upload new vehicle.
4) Search vehicles and see their details and focus on the map.
## Features - optional
1) Public chat with the owner of the vehicle (which have been found in the search process).
2) Additional information about specific vehicle from free API.

# Design
## Description
FrontEnd with HTML, BackEnd with Flask (Python 3) and Database with SQLite (SQLAlchemy).
The package 'website' contains the all application. The main file (main.py) imports website and the function create_app(app), which creates the package, the database and initializes the blueprints. The application is divided into 2 Blueprints: auth and views
auth handles the operations: login, signup and logout. <br />
views handles the operations: Display/Delete user profile, Upload/Delete vehicle, Search vehicles, Display analytics (Heat Map page).

## Database diagram
<img width="431" alt="image" src="https://user-images.githubusercontent.com/58309185/193948888-cbfe583a-2bd4-4a97-b8b6-9ae058bb8c6d.png">

## Sequence diagrams
![image](https://user-images.githubusercontent.com/58309185/193948928-cfce9eed-0292-4cc3-bb1e-12d7c90be3a4.png)

![image](https://user-images.githubusercontent.com/58309185/193948955-b830e5b3-df0c-4aba-9b69-362d8ad31811.png)

![image](https://user-images.githubusercontent.com/58309185/193948987-ca09010e-92f4-4f74-aa0b-40b838196c13.png)

![image](https://user-images.githubusercontent.com/58309185/193949007-6dfbe82a-f76a-4266-9fab-186e1412da51.png)

![image](https://user-images.githubusercontent.com/58309185/193949036-d14bcd9f-6108-4ba0-b205-cb11d15cd891.png)

# Deployment - run in CMD:
** copy the lines below to cmd in this order!
python -m set_up.py
python -m pip install --upgrade pip
python .\run_setup.py
python -m venv env
\venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --force-reinstall
python -m main
