import os


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vapecloud.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
