

class Config:
    SECRET_KEY = '1230'
    DATABASE_URI = 'sqlite:///db.sqlite3'


class ProductionConfig(Config):
    # DB_SERVER = 'localhost'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True