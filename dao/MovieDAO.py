from my_project.db_init import db
from my_project.auth.models.movie import Movie


class MovieDAO:


    def get_all(self):
        return Movie.query.all()


    def get_by_id(self, movie_id):
        return Movie.query.get(movie_id)


    def create(self, data):
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie


    def update(self, movie_id, data):
        movie = Movie.query.get(movie_id)
        if movie:
            for key, value in data.items():
                setattr(movie, key, value)
            db.session.commit()
            return movie
        return None


    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return True
        return False
