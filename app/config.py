import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #pegar pasta raiz

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'messages.db')}" #define o local do bd
    SQLALCHEMY_TRACK_MODIFICATIONS = False #evita avisos desnecessarios