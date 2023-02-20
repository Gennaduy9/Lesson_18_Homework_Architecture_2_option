from flask import Flask
from flask_restx import Api

from app.config import Config

from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie

from app.setup_db import db

from app.views.movies import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns


# функция создания основного объекта app
def create_app(config_object):
     app = Flask(__name__)
     app.config.from_object(config_object)
     register_extensions(app)
     return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
     db.init_app(app)
     api = Api(app)
     api.add_namespace(movie_ns)
     api.add_namespace(genre_ns)
     api.add_namespace(director_ns)
     create_data(app, db)


def create_data(app, db):
    with app.app_context():
         db.drop_all()
         db.create_all()

         m1 = Movie(id=1, title="Мулен Руж", description="Париж, 1899 год. Знаменитый ночной клуб «Мулен Руж» — это не только дискотека и шикарный бордель, но и место, где, повинуясь неудержимому желанию прочувствовать атмосферу праздника, собираются страждущие приобщиться к красоте, свободе, любви и готовые платить за это наличными.",
                    trailer="https://www.youtube.com/watch?v=lpiMCTd87gE", year=2001, rating=7.6, genre_id=18, director_id=7)
         m2 = Movie(id=2, title="Одержимость", description="Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?",
                    trailer="https://www.youtube.com/watch?v=Q9PxDPOo1jw", year=2013, rating=8.5, genre_id=4, director_id=8)

         d1 = Director(id=1, name="Harry Potter")
         d2 = Director(id=2, name="Le Comte de Monte-Cristo")

         g1 = Genre(id=1, name="Робин Уильямс")
         g2 = Genre(id=2, name="Том Круз")


         with db.session.begin():
             db.session.add_all([m1, m2])
             db.session.add_all([d1, d2])
             db.session.add_all([g1, g2])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
     app.run(host="localhost", port=10002, debug=True)


