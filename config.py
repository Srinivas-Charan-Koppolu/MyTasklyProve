import os

RENDER_DB_URL = 'postgresql://srinivascharank_mytasklyprove:YaQZez9J2hZrdqG6Ja7wb9TfLwoCi6EM@dpg-d0or5i6uk2gs73903s60-a/mytasklyprove'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
DB_PATH = os.path.join(INSTANCE_DIR, 'mytasklyprove.db')


# Make sure instance folder exists
if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mytasklyprove-secret')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        RENDER_DB_URL
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Routes Enable/Disable
    ENABLE_AUTH = True
    ENABLE_DASHBOARD = True

