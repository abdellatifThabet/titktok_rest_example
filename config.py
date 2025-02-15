import os

class ConfigApp(object):
    # generic
    CSRF_ENABLED = os.environ.get('CSRF_ENABLED', False)
    API_KEY = os.environ['API_KEY']

    DEBUG = os.environ.get('DEBUG', False)
    TESTING = os.environ.get('TESTING', False)

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = ConfigApp()