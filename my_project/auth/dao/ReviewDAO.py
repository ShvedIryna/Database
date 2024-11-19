from my_project.db_init import db
from my_project.auth.models.review import Review

class ReviewDAO:
    def get_all(self):
        return Review.query.all()

    def get_by_id(self, review_id):
        return Review.query.get(review_id)

    def create(self, data):
        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    def update(self, review_id, data):
        review = Review.query.get(review_id)
        if review:
            for key, value in data.items():
                setattr(review, key, value)
            db.session.commit()
            return review
        return None

    def delete(self, review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False

    def get_reviews_by_movie(self, movie_id):
        return Review.query.filter(Review.movie_id == movie_id).all()
