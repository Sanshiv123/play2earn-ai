import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///play2earn.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
