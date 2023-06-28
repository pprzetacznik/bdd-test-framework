from os import getenv
from my_app.server import create_app
from my_app.settings import TestConfig, DevConfig, ProdConfig

config_options = {"test": TestConfig, "dev": DevConfig, "prod": ProdConfig}

app = create_app(config_options.get(getenv("FLASK_ENV")))
