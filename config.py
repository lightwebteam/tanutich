from app import tanutich

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'yo-tanutich-2-sick'
    tanutich.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    tanutich.config['SQLALCHEMY_ECHO'] = False
    tanutich.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:2378951@localhost/flask_train'