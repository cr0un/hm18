from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns


def register_extensions(app):
    api = Api(app)
    db.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


if __name__ == '__main__':
    app = create_app(Config())
    app.debug = True
    app.run(host="localhost", port=10001, debug=False)
