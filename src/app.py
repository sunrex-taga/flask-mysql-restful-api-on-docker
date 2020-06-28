from flask import Flask, jsonify

from flask_restful import Api

from src.database import init_db

from src.apis.users import UsersListAPI, UsersAPI
from src.apis.rooms import RoomsListAPI, RoomsAPI
from src.apis.schedules import SchedulesListAPI, SchedulesAPI
from src.apis.roominfo import RoomInfoListAPI, RoomInfoAPI

def create_app():

  app = Flask(__name__)
  app.config.from_object('src.config.Config')
  app.config['JSON_AS_ASCII'] = False

  init_db(app)

  api = Api(app)
  api.add_resource(UsersListAPI, '/users')
  api.add_resource(UsersAPI, '/users/<id>')
  api.add_resource(RoomsListAPI, '/rooms')
  api.add_resource(RoomsAPI, '/rooms/<id>')
  api.add_resource(SchedulesListAPI, '/schedules')
  api.add_resource(SchedulesAPI, '/schedules/<id>')
  api.add_resource(RoomInfoListAPI, '/roominfo')
  api.add_resource(RoomInfoAPI, '/roominfo/<id>')

  return app


app = create_app()
