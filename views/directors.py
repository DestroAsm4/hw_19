from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service
from utils import auth_require, admin_require

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    @auth_require
    def get(self):
        print(director_service.get_all())
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_require
    def post(self):
        data = request.json
        director_service.create(data)
        return '', 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_require
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_require
    def put(self, did):
        data = request.json
        if 'id' not in data:
            data['id'] = did
        director_service.update(data)
        return '', 204

    @admin_require
    def delete(self, did):
        director_service.delete(did)
        return '', 204
