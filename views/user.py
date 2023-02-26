from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

@user_ns.route('/')
class UsersViwe(Resource):

    def get(self):
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)
        return result, 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201

@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        return res, 200

    def put(self, uid):
        data = request.json
        if 'id' not in data:
            data['id'] = uid
        user_service.update(data)
        return '', 204

    def delete(self, uid):
        user_service.delete(uid)
        return '', 204
