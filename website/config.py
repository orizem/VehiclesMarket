import os

SECRET_KEY = '9OLWxND4o83j4K4iuopO'
DB_NAME = 'db.sqlite'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBSITE_PATH = os.path.abspath(os.path.dirname(DB_NAME))