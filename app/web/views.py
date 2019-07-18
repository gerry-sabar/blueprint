from . import web
from flask import render_template


# localhost:5000 will access this entrypoint & render template from login.html
@web.route('/')
def login():
    return render_template('login.html')
