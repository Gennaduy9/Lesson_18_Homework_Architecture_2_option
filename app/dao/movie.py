from app.dao.model.movie import Movie


# MOVIE
class MovieDAO:
    def __init__(self, session):
        self.session = session
        self.model = Movie


    def get_my_id(self, mid):
        return self.session.query(self.model).get(mid)


    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['director_id']
            ).all()
        elif filters['genre_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['genre_id']
            ).all()
        elif filters['year']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['year']
            ).all()

        return self.session.query(self.model).all()


    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie


    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_my_id(mid)

        self.session.delete(movie)
        self.session.commit()