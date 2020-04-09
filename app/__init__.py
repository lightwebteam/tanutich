from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

tanutich = Flask(__name__)


from config import Config
tanutich.config.from_object(Config)
db = SQLAlchemy(tanutich)

# login = LoginManager(tanutich)



from app import views, models