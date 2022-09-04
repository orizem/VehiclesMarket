import os

# GET PATH TO FOLDER, FORMATTED
PATH = os.getcwd().replace('\\','/').replace(' ', '%20')

LIBS = '''asgiref==3.5.2
asttokens==2.0.8
attrs==22.1.0
backcall==0.2.0
branca==0.5.0
certifi==2022.6.15
charset-normalizer==2.1.1
click==8.1.3
click-plugins==1.1.1
cligj==0.7.2
colorama==0.4.5
cycler==0.11.0
debugpy==1.6.3
decorator==5.1.1
Django==4.1
entrypoints==0.4
executing==1.0.0
Fiona @ file:///PATH/wheels/Fiona-1.8.21-cp39-cp39-win_amd64.whl
Flask==2.2.2
Flask-Login==0.6.2
Flask-SQLAlchemy==2.5.1
folium==0.12.1.post1
fonttools==4.37.1
GDAL @ file:///PATH/wheels/GDAL-3.4.3-cp39-cp39-win_amd64.whl
geopandas==0.11.1
greenlet==1.1.3
idna==3.3
importlib-metadata==4.12.0
ipykernel==6.15.2
ipython==8.4.0
itsdangerous==2.1.2
jedi==0.18.1
Jinja2==3.1.2
joblib==1.1.0
jupyter-core==4.11.1
jupyter_client==7.3.5
kiwisolver==1.4.4
mapclassify==2.4.3
MarkupSafe==2.1.1
matplotlib==3.5.3
matplotlib-inline==0.1.6
munch==2.5.0
nest-asyncio==1.5.5
networkx==2.8.6
numpy==1.23.2
packaging==21.3
pandas==1.4.3
parso==0.8.3
pickleshare==0.7.5
Pillow==9.2.0
prompt-toolkit==3.0.30
psutil==5.9.1
pure-eval==0.2.2
Pygments==2.13.0
pyparsing==3.0.9
pyproj==3.3.1
python-dateutil==2.8.2
python-dotenv==0.20.0
pytz==2022.2.1
pywin32==304
pyzmq==23.2.1
requests==2.28.1
Rtree==1.0.0
scikit-learn==1.1.2
scipy==1.9.1
Shapely==1.8.4
six==1.16.0
SQLAlchemy==1.4.40
sqlparse==0.4.2
stack-data==0.5.0
threadpoolctl==3.1.0
tornado==6.2
traitlets==5.3.0
tzdata==2022.2
urllib3==1.26.12
wcwidth==0.2.5
Werkzeug==2.2.2
zipp==3.8.1'''.replace('PATH', PATH)