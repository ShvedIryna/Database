from flask import Flask
from __init__ import create_app
from my_project.auth.route.movie_route import movie_bp
from my_project.auth.route.actor_route import actor_bp
from my_project.auth.route.movie_actor_route import movie_actor_bp
from my_project.auth.route.review_route import review_bp
from my_project.auth.route.rating_route import rating_bp
from my_project.auth.route.user_route import user_bp
from my_project.auth.route.country_route import country_bp
from my_project.auth.route.genre_route import genre_bp
from my_project.auth.route.box_office_route import box_office_bp
from my_project.auth.route.movie_genre_route import movie_genre_bp
from my_project.auth.route.TableRoutes import table_bp

app = create_app()

app.register_blueprint(movie_bp)
app.register_blueprint(actor_bp)
app.register_blueprint(movie_actor_bp)
app.register_blueprint(review_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(user_bp)
app.register_blueprint(country_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(box_office_bp)
app.register_blueprint(movie_genre_bp)
app.register_blueprint(table_bp)

if __name__ == '__main__':
    app.run(debug=False)
