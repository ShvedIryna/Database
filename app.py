from flask import Flask
from __init__ import create_app
from my_project.auth.route.movie_route import movie_bp
from my_project.auth.route.actor_route import actor_bp
from my_project.auth.route.movie_actor_route import movie_actor_bp
from my_project.auth.route.review_route import review_bp


app = create_app()

app.register_blueprint(movie_bp)
app.register_blueprint(actor_bp)
app.register_blueprint(movie_actor_bp)
app.register_blueprint(review_bp)

if __name__ == '__main__':
    app.run(debug=False)

