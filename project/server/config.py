# project/server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))
# postgres_local_base = 'postgresql://postgres:@localhost/'
# sqlite_local_base = 'sqlite:///' + basedir + '\\'
sqlite_local_base = 'mysql+pymysql://root:Admin@123@localhost:3307/'
database_name = 'flask_auth_db'

# EmailID
serviceEmail = 'xxxx@gmail.com'
password = '********'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_local_base + database_name + '_dev'

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'super_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = sqlite_local_base + database_name
