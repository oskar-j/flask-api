import os


class Config(object):
    # Flask settings
    FLASK_DEBUG = False
    DEBUG = False
    TESTING = False

    USE_RELOADER = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    DEBUG = True

    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_ECHO = False


class SqlLiteDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class TestingConfig(Config):
    TESTING = True

    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_ECHO = False
