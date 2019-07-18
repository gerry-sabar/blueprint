from flask import Blueprint

# creating blueprint instance for web module
web = Blueprint('web', __name__)

from . import views
