from flask import request
from flask_restx import Resource, Namespace
from dao.model.movies import Movie_Schema
from implemented import movie_service


movie_ns = Namespace("movies")


@movie_ns.route("/")
class Movies_view(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        filter = {
            "director_id": director,
            "genre_id": genre,
            "year": year
        }

        all_movies = movie_service.get_all(filter)
        result = Movie_Schema(many=True).dump(all_movies)
        return result, 200


    def post(self):
        request_json = request.json
        print("request_json:", request_json)
        movie = movie_service.create(request_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route("/<int:uid>")
class Movie_view(Resource):
    def get(self, uid):
        obj = movie_service.get_one(uid)
        result = Movie_Schema().dump(obj)
        return result, 200


    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid
        movie_service.update(request_json)
        return "", 204


    def delete(self, uid):
        movie_service.delete(uid)
        return "", 204


