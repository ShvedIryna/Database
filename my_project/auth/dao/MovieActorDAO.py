from my_project.db_init import db
from my_project.auth.models.movie_actor import Movie_Actor

class MovieActorDAO:
    def get_all(self):
        return Movie_Actor.query.all()

    def get_by_movie_and_actor(self, movie_id, actor_id):
        return Movie_Actor.query.get((movie_id, actor_id))

    def create(self, data):
        new_entry = Movie_Actor(**data)
        db.session.add(new_entry)
        db.session.commit()
        return new_entry

    def update(self, movie_id, actor_id, data):
        entry = Movie_Actor.query.get((movie_id, actor_id))
        if entry:
            for key, value in data.items():
                setattr(entry, key, value)
            db.session.commit()
            return entry
        return None

    def delete(self, movie_id, actor_id):
        entry = Movie_Actor.query.get((movie_id, actor_id))
        if entry:
            db.session.delete(entry)
            db.session.commit()


    def get_actors_by_movie(self, movie_id):
        return Movie_Actor.query.filter_by(movie_id=movie_id).all()


    def get_movies_by_actor(self, actor_id):
        return Movie_Actor.query.filter_by(actor_id=actor_id).all()
