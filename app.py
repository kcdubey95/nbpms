
from flask import Flask
from flask_migrate import Migrate
from routes import main
from db_config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate =Migrate(app,db)


def register_resources(app):
    app.register_blueprint(main)


if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
