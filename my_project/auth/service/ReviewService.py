from my_project.auth.dao.ReviewDAO import ReviewDAO

class ReviewService:
    def __init__(self):
        self.review_dao = ReviewDAO()

    def get_all_reviews(self):
        return self.review_dao.get_all()

    def get_review_by_id(self, review_id):
        return self.review_dao.get_by_id(review_id)

    def create_review(self, data):
        return self.review_dao.create(data)

    def update_review(self, review_id, data):
        return self.review_dao.update(review_id, data)

    def delete_review(self, review_id):
        return self.review_dao.delete(review_id)

    def get_reviews_by_movie(self, movie_id):
        reviews = self.review_dao.get_reviews_by_movie(movie_id)
        if not reviews:
            return None, 'No reviews found for this movie'
        return [review.to_dict() for review in reviews], None