from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.users import UsersModel, UsersSchema

from src.database import db


class UsersListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    self.reqparse.add_argument('state', required=True)
    super(UsersListAPI, self).__init__()


  def get(self):
    results = UsersModel.query.all()
    print(UsersSchema(many=True).dump(results))
    jsonData = UsersSchema(many=True).dump(results)
    return jsonify({'items': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    users = UsersModel(args.name, args.state)
    db.session.add(users)
    db.session.commit()
    res = UsersSchema().dump(users).data
    return res, 201


class UsersAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    self.reqparse.add_argument('state')
    super(UsersAPI, self).__init__()


  def get(self, id):
    users = db.session.query(UsersModel).filter_by(id=id).first()
    if users == None:
      abort(404)

    res = UsersSchema().dump(users)
    return res


  def put(self, id):
    users = db.session.query(UsersModel).filter_by(id=id).first()
    if users == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(users, name, value)
    db.session.add(users)
    db.session.commit()
    return None, 204


  def delete(self, id):
    users = db.session.query(UsersModel).filter_by(id=id).first()
    if users is not None:
      db.session.delete(users)
      db.session.commit()
    return None, 204
