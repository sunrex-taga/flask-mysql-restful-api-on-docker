import os


class DevelopmentConfig:

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'admin'),
      'password': os.getenv('DB_PASSWORD', 'Sunrex3094'),
      'host': os.getenv('DB_HOST', 'conference2020a.cbauvghl3wuk.ap-northeast-1.rds.amazonaws.com'),
      'database': os.getenv('DB_DATABASE', 'conference_room_develop'),
    })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False


Config = DevelopmentConfig