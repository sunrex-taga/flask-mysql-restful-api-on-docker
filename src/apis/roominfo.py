from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.roominfo import RoomInfoModel, RoomInfoSchema

from src.database import db


class RoomInfoListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('rooms_id', required=True)
    self.reqparse.add_argument('data')
    super(RoomInfoListAPI, self).__init__()


  def get(self):
    results = RoomInfoModel.query.all()
    jsonData = RoomInfoSchema(many=True).dump(results)
    return jsonify({'res': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    roominfo = RoomInfoModel(args.rooms_id, args.data)
    db.session.add(roominfo)
    db.session.commit()
    res = RoomInfoSchema().dump(roominfo).data
    return res, 201


class RoomInfoAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('rooms_id')
    self.reqparse.add_argument('data')
    super(RoomInfoAPI, self).__init__()


  def get(self, id):
    roominfo = db.session.query(RoomInfoModel).filter_by(id=id).first()
    if roominfo == None:
      abort(404)

    res = RoomInfoSchema().dump(roominfo)
    return jsonify({'res': res})
    # return res


  def put(self, id):
    roominfo = db.session.query(RoomInfoModel).filter_by(id=id).first()
    if roominfo == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(roominfo, name, value)
    db.session.add(roominfo)
    db.session.commit()
    return None, 204


  def delete(self, id):
    roominfo = db.session.query(RoomInfoModel).filter_by(id=id).first()
    if roominfo is not None:
      db.session.delete(roominfo)
      db.session.commit()
    return None, 204
