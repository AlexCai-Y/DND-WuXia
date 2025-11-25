from flask import Flask
from .db import init_db, close_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE="combat.sqlite"
    )


    return app