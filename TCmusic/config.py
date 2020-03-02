import os


class Config:
    SECRET_KEY = "mrsoft"
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(app):
        pass


# 用于开发的配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/music"
    DEBUG = True


# 定义配置
config = {
    "default": DevelopmentConfig
}