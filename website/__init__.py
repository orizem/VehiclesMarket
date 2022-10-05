# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_bootstrap import Bootstrap

from .config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, DB_NAME
from os import path

bootstrap = Bootstrap()

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    bootstrap.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    create_database(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    from .views import page_not_found
    # page not found
    app.register_error_handler(404, page_not_found)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app


def create_database(app):
    if not path.exists(f'website/{DB_NAME}'):
        db.create_all(app=app)
        print('Database has been created')