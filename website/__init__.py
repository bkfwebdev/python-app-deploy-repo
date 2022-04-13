from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
from flask_migrate import Migrate
#DB_NAME = "restaurauntbuddy"
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    Migrate.init_app(app, db)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://ruzouuemtotljl:0ff662697a7a1f4cbf22dff699770508865457921c0690195ea8526409013284@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d36aemg0ue2hkv') or \
            'sqlite:///' + os.path.join(app.instance_path, 'task_list.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    #db.init_app(app)
    #Migrate.init_app(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Favorite

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    
  



