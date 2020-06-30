from datetime import datetime

from flask_marshmallow import Marshmallow

from flask_marshmallow.fields import fields

# from sqlalchemy_utils import UUIDType

from src.database import db

# import uuid

ma = Marshmallow()


class RoomsModel(db.Model):
  __tablename__ = 'rooms'
  __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(20), nullable=False)
  # map_image = db.Column(db.String(255), nullable=False)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, name, state):
    self.name = name


  def __repr__(self):
    return '<RoomsModel {}:{}>'.format(self.id, self.name)

class Rooms2Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "id2", "rooms_id", "data")

class RoomsSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = RoomsModel
    load_instance = True

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
