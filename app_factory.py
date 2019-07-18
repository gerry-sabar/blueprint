import os
from flask_migrate import Migrate
#import create_app & db from app/__init__.py in directory
from app import create_app, db

#this part will refer to config.py
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

#will be used to run migration later
migrate = Migrate(app, db)