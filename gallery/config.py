# we're gonna keep global variables that we want for the application use in here
class Config(object):
    SQLALCHEMY_DATABASE_URI = '*'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '*'
    AZURE_STORAGE_ACCOUNT_NAME = '*'
    AZURE_STORAGE_ACCOUNT_KEY = '*'
    AZURE_STORAGE_CONTAINER_NAME = '*'
    AZURE_STORAGE_CONTAINER_LOCATION = '*'
    ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}
