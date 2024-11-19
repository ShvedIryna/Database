from flask import request, jsonify
from my_project.auth.service.ReviewService import ReviewService

review_service = ReviewService()

def get_all_reviews():
    reviews = review_service.get_all_reviews()
    return jsonify([review.to_dict() for review in reviews]), 200

def get_review_by_id(review_id):
    review = review_service.get_review_by_id(review_id)
    if review:
        return jsonify(review.to_dict()), 200
    return jsonify({'message': 'Review not found'}), 404

def create_review():
    data = request.json
    new_review = review_service.create_review(data)
    return jsonify(new_review.to_dict()), 201

def update_review(review_id):
    data = request.json
    updated_review = review_service.update_review(review_id, data)
    if updated_review:
        return jsonify(updated_review.to_dict()), 200
    return jsonify({'message': 'Review not found'}), 404

def delete_review(review_id):
    success = review_service.delete_review(review_id)
    if success:
        return jsonify({'message': 'Review deleted successfully'}), 200
    return jsonify({'message': 'Review not found'}), 404

def get_reviews_by_movie(movie_id):
    data, error = review_service.get_reviews_by_movie(movie_id)
    if error:
        return jsonify({'error': error}), 404
    return jsonify(data), 200
