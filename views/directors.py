from flask_restx import Resource, Namespace
from dao.model.directors import Director_Schema
from implemented import director_service


director_ns = Namespace("directors")


@director_ns.route("/")
class Directors_view(Resource):
    def get(self):
        directors = director_service.get_all()
        result = Director_Schema(many=True).dump(directors)
        return result, 200


@director_ns.route("/<int:uid>")
class Director_view(Resource):
    def get(self, uid):
        director = director_service.get_one(uid)
        result = Director_Schema(many=False).dump(director)
        return result, 200


