import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
