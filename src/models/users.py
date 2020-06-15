from datetime import datetime

from flask_marshmallow import Marshmallow

from flask_marshmallow.fields import fields

# from sqlalchemy_utils import UUIDType

from src.database import db

# import uuid

ma = Marshmallow()


class UsersModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False)
  state = db.Column(db.String(255), nullable=False)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, name, state):
    self.name = name
    self.state = state


  def __repr__(self):
    return '<UsersModel {}:{}>'.format(self.id, self.name)


class UsersSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = UsersModel
    load_instance = True

# class UsersSchema(ma.ModelSchema):
#   class Meta:
#     model = UsersModel

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')