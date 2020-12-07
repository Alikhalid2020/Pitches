import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY='SECRET_KEY'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Morninga:Alikhalid3436@localhost/pitches'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://morninga:Alikhalid3436@localhost/pitches'
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}