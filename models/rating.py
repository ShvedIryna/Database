from my_project.db_init import db
from my_project.auth.models.movie import Movie
from my_project.auth.models.user import User


class Rating(db.Model):
    __tablename__ = 'rating'

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    movie = db.relationship('Movie', backref=db.backref('ratings', cascade='all, delete-orphan'))
    user = db.relationship('User', backref=db.backref('ratings', cascade='all, delete-orphan'))

    def to_dict(self):
        return {
            "rating_id": self.rating_id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
            "rating": self.rating,
        }


class RatingLog(db.Model):
    __tablename__ = 'rating_log'

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating_id = db.Column(db.Integer, nullable=False)
    old_rating = db.Column(db.Integer, nullable=False)
    new_rating = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
