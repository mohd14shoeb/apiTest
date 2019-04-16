import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = "postgresql://localhost/"
database_name = "apiTestDb"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "asd765-876fk-jmncn456-vbs98dj-766fsdf")
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True