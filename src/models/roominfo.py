from datetime import datetime

from flask_marshmallow import Marshmallow

from flask_marshmallow.fields import fields

# from sqlalchemy_utils import UUIDType

from src.database import db

# import uuid

ma = Marshmallow()


class RoomInfoModel(db.Model):
  __tablename__ = 'roominfo'
  __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  rooms_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
  data = db.Column(db.String(30), nullable=False)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, rooms_id, data):
    self.rooms_id = rooms_id
    self.data = data


  def __repr__(self):
    return '<RoomInfoModel {}:{}>'.format(self.id, self.data)


class RoomInfoSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = RoomInfoModel
    load_instance = True

# class RoomInfoSchema(ma.ModelSchema):
#   class Meta:
#     model = RoomInfoModel

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
