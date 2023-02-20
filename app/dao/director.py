from app.dao.model.director import Director


# DIRECTOR
class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.model = Director


    def get_my_id(self, did):
        return self.session.query(self.model).get(did)


    def get_all(self):
        return self.session.query(self.model).all()


    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director


    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, did):
        director = self.get_my_id(did)

        self.session.delete(director)
        self.session.commit()