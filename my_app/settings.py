class Config:
    ENV = "dev"
    DEBUG = True


class TestConfig(Config):
    ENV = "test"
    DEBUG = True


class DevConfig(Config):
    ENV = "dev"
    DEBUG = True


class ProdConfig(Config):
    ENV = "prod"
    DEBUG = False
