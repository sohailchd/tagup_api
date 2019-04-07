from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_heroku import Heroku

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__,static_url_path="/app/main/templates/statics")
    app.config.from_object(config_by_name[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print(f"current env : {config_name}")
    if config_name=="prod":
        heroku = Heroku(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app