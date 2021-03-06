from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.rooms import RoomsModel, RoomsSchema, Rooms2Schema
from src.models.roominfo import RoomInfoModel, RoomInfoSchema

from src.database import db


class RoomsListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    super(RoomsListAPI, self).__init__()


  def get(self):
    results = RoomsModel.query.all()
    jsonData = RoomsSchema(many=True).dump(results)
    return jsonify({'res': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    rooms = RoomsModel(args.name)
    db.session.add(rooms)
    db.session.commit()
    res = RoomsSchema().dump(rooms).data
    return res, 201


class RoomsAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    super(RoomsAPI, self).__init__()


  def get(self, id):
    rooms = db.session.query(RoomsModel).filter_by(id=id).first()
    if rooms == None:
      abort(404)

    res = RoomsSchema().dump(rooms)
    return jsonify({'res': res})
    # return res

  def put(self, id):
    rooms = db.session.query(RoomsModel).filter_by(id=id).first()
    if rooms == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(rooms, name, value)
    db.session.add(rooms)
    db.session.commit()
    return None, 204


  def delete(self, id):
    rooms = db.session.query(RoomsModel).filter_by(id=id).first()
    if rooms is not None:
      db.session.delete(rooms)
      db.session.commit()
    return None, 204

class Rooms2API(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    super(Rooms2API, self).__init__()


  def get(self, id):
    # rooms = db.session.query(RoomsModel).filter_by(id=id).first()
    rooms = db.session.query(RoomsModel, RoomInfoModel).join(RoomsModel, RoomsModel.id == RoomInfoModel.rooms_id).filter_by(id=id).order_by(RoomInfoModel.createTime.desc()).first()
    if rooms == None:
      abort(404)

    res = RoomInfoSchema().dump(rooms.RoomInfoModel)
    res2 = RoomsSchema().dump(rooms.RoomsModel)
    res.update(res2)
    return jsonify({'res': res})
    # return res
