from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import config from config.py we created before to be implemented in create_app
from config import config

db = SQLAlchemy()


def create_app(config_name):
    #we add template from folder templates inside app directory
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #example how to display web page with template from web module inside app directory
    from .web import web as main_blueprint
    app.register_blueprint(main_blueprint)

    #exmample how to implement RESTful API with swagger from api module inside app directory
    from .api import api as auth_blueprint
    #we add prefix api for our API so will be like localhost:5000/api
    app.register_blueprint(auth_blueprint, url_prefix='/api')

    db.init_app(app)

    return app
