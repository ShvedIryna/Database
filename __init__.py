from flask import Flask
from my_project.db_init import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pasle2006@localhost/MovieDB'

    db.init_app(app)

    return app
