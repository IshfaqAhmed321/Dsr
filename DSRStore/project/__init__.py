import os

from flask import Flask 
from flask_login import LoginManager

from .models import db
from .models import User
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .admin import admin as admin_blueprint
from .user import user as user_blueprint

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "9OLWxND4o83j4K4iuopO"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sql12313574:fRzx6yXGtd@sql12.freemysqlhosting.net/sql12313574"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
  
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(user_blueprint)
    
    return app
