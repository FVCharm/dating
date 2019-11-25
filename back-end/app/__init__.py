from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)

    register_db(app)

    from app.api import bp
    app.register_blueprint(bp, url_prefix='/v1')

    return app


def register_db(app):
    from app.models.base import db
    db.init_app(app)
    migrate.init_app(app, db)


from app.models import user

