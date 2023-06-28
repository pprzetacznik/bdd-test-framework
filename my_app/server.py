import logging
from flask import Flask
from my_app import users
from my_app.settings import DevConfig


def register_logger():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logger initialized")


def register_blueprints(app):
    blueprints = [
        users.views.blueprint,
    ]
    for bp in blueprints:
        app.register_blueprint(bp)


def create_app(config):
    register_logger()
    app = Flask(__name__)
    logging.getLogger("werkzeug").handlers.clear()
    app.config.from_object(config)
    register_blueprints(app)
    app.config["config"] = config
    return app


if __name__ == "__main__":
    app = create_app(DevConfig)
    app.run(host="0.0.0.0", port=8002)
