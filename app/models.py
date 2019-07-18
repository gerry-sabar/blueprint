from . import db
from sqlalchemy import (Text)  # you can add another table column type if you need
from marshmallow import Schema, fields as FM  # will be used to serialize JSON 


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(Text)


class LogSchema(Schema):
    id = FM.Int()
    detail = FM.Str()
