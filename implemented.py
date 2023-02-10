# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService

from setup_db import db

genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)



