import os


class Config:
    SECRET_KEY = '32a30c75fbbc1cedb4b3f252768c80b0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'alwaysbecoolandhappy@gmail.com'
    MAIL_PASSWORD = 'Manik!9515'