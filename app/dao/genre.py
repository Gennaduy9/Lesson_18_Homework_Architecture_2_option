from app.dao.model.genre import Genre


# GENRE
class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.model = Genre


    def get_my_id(self, gid):
        return self.session.query(self.model).get(gid)


    def get_all(self):
        return self.session.query(self.model).all()


    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre


    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, gid):
        genre = self.get_my_id(gid)

        self.session.delete(genre)
        self.session.commit()