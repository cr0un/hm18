from flask_restx import Resource, Namespace
from dao.model.genres import Genre_Schema
from implemented import genre_service


genre_ns = Namespace("genres")


@genre_ns.route("/")
class Genres_view(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = Genre_Schema(many=True).dump(genres)
        return result, 200


@genre_ns.route("/<int:uid>")
class Genres_view(Resource):
    def get(self, uid):
        genre = genre_service.get_one(uid)
        result = Genre_Schema(many=False).dump(genre)
        return result, 200


