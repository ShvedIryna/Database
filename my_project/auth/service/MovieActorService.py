from my_project.auth.dao.MovieActorDAO import MovieActorDAO

class MovieActorService:
    def __init__(self):
        self.movie_actor_dao = MovieActorDAO()

    def get_all_entries(self):
        return self.movie_actor_dao.get_all()

    def get_entry_by_ids(self, movie_id, actor_id):
        return self.movie_actor_dao.get_by_movie_and_actor(movie_id, actor_id)

    def create_entry(self, data):
        return self.movie_actor_dao.create(data)

    def update_entry(self, movie_id, actor_id, data):
        return self.movie_actor_dao.update(movie_id, actor_id, data)

    def delete_entry(self, movie_id, actor_id):
        return self.movie_actor_dao.delete(movie_id, actor_id)

    def get_actors_by_movie(self, movie_id):
        actors = self.movie_actor_dao.get_actors_by_movie(movie_id)
        if not actors:
            return None, 'No actors found for this movie'
        return [actor.to_dict() for actor in actors], None

    def get_movies_by_actor(self, actor_id):
        movies = self.movie_actor_dao.get_movies_by_actor(actor_id)
        if not movies:
            return None, 'No movies found for this actor'

        # Ітерація по списку фільмів
        return [movie.to_dict() for movie in movies], None