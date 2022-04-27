from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'siunimtauchumkiubiuje'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:Over9000@localhost:5432/{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ruzouuemtotljl:0ff662697a7a1f4cbf22dff699770508865457921c0690195ea8526409013284@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d36aemg0ue2hkv'



    db.init_app(app)

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
    #if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    
    
  



