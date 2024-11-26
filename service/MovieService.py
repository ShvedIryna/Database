from my_project.auth.dao.MovieDAO import MovieDAO

class MovieService:
    def __init__(self):
        self.movie_dao = MovieDAO()

    def get_all_movies(self):
        return self.movie_dao.get_all()

    def get_movie_by_id(self, movie_id):
        return self.movie_dao.get_by_id(movie_id)

    def create_movie(self, data):
        return self.movie_dao.create(data)

    def update_movie(self, movie_id, data):
        return self.movie_dao.update(movie_id, data)

    def delete_movie(self, movie_id):
        return self.movie_dao.delete(movie_id)
