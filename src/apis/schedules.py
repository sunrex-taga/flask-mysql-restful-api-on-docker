from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.schedules import SchedulesModel, SchedulesSchema

from src.database import db


class SchedulesListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('rooms_id', required=True)
    self.reqparse.add_argument('rooms_name')
    self.reqparse.add_argument('users_id', required=True)
    self.reqparse.add_argument('reserved_person')
    self.reqparse.add_argument('title', required=True)
    # self.reqparse.add_argument('createTime')
    # self.reqparse.add_argument('updateTime')
    super(SchedulesListAPI, self).__init__()


  def get(self):
    results = SchedulesModel.query.all()
    # print(SchedulesSchema(many=True).dump(results))
    jsonData = SchedulesSchema(many=True).dump(results)
    return jsonify({'res': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    schedules = SchedulesModel(args.rooms_id, args.rooms_name, args.users_id, args.reserved_person, args.title)
    db.session.add(schedules)
    db.session.commit()
    res = SchedulesSchema().dump(schedules)
    return res, 201


class SchedulesAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('rooms_id')
    self.reqparse.add_argument('rooms_name')
    self.reqparse.add_argument('users_id')
    self.reqparse.add_argument('reserved_person')
    self.reqparse.add_argument('title')
    super(SchedulesAPI, self).__init__()


  def get(self, id):
    schedules = db.session.query(SchedulesModel).filter_by(id=id).first()
    if schedules == None:
      abort(404)

    res = SchedulesSchema().dump(schedules)
    return jsonify({'res': res})
    # return res


  def put(self, id):
    schedules = db.session.query(SchedulesModel).filter_by(id=id).first()
    if schedules == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(schedules, name, value)
    db.session.add(schedules)
    db.session.commit()
    return None, 204


  def delete(self, id):
    schedules = db.session.query(SchedulesModel).filter_by(id=id).first()
    if schedules is not None:
      db.session.delete(schedules)
      db.session.commit()
    return None, 204
