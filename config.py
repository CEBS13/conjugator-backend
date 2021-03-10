import os
basedir = os.path.abspath(os.path.dirname((__file__))


class Config(Object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ssssss'
    SQLALCHEMY_DATABASE_URI = os.envrion["postgresql:///conjugator_db"]

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
    
