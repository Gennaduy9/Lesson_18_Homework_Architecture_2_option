from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200



@genre_ns.route('/<int:gid>')
class MovieView(Resource):
    def get(self, gid: int):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as g:
            return str(g), 404