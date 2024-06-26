import os
from flask import Flask 
from flask_socketio import SocketIO, emit

from .base import db
from .routes import main



def create_app():

    print('Loading Routes..... , Please Wait')

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')      # SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')    # URI

    socketio = SocketIO(app, cors_allowed_origins='*')
    db.init_app(app)
    app.register_blueprint(main)
    return app
