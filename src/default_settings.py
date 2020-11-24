import os
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SQlALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DATABASE_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

# def init_db(app):
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     db = SQLAlchemy(app)
#     return db
