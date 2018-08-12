import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfiguration(Config):
    """Development configuration class."""
    DEBUG = True
    DEVELOPMENT = True


class TestingConfiguration(Config):
    """Development configuration class."""
    TESTING = True


class ProductionConfiguration(Config):
    """Development configuration class."""
    DEBUG = False


app_configuration = {
    'production': ProductionConfiguration,
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration
}
