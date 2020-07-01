from datetime import datetime

from flask_marshmallow import Marshmallow

from flask_marshmallow.fields import fields

# from sqlalchemy_utils import UUIDType

from src.database import db

# import uuid

ma = Marshmallow()


class SchedulesModel(db.Model):
  __tablename__ = 'schedules'
  # __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  rooms_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
  rooms_name = db.Column(db.String(20), nullable=False)
  users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  reserved_person = db.Column(db.String(30), nullable=False)
  title = db.Column(db.String(50), nullable=False)
  started_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  ended_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, rooms_id, rooms_name, users_id, reserved_person, title, started_at, ended_at):
    self.rooms_id = rooms_id
    self.rooms_name = rooms_name
    self.users_id = users_id
    self.reserved_person = reserved_person
    self.title = title
    self.started_at = started_at
    self.ended_at = ended_at


  def __repr__(self):
    return '<SchedulesModel {}:{}>'.format(self.id, self.rooms_name)


class SchedulesSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = SchedulesModel
    load_instance = True
    include_fk = True

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  started_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  ended_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
