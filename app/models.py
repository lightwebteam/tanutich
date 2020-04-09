# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
from app import db

class User(db.Model):
    __tablename__ = 'users_test'  # назначили имя таблицы
    id = db.Column(db.Integer, primary_key=True)  # создаем колонки в бд
    username = db.Column(db.String(20), index=True, unique=True)  # 20 символов
    password = db.Column(db.String(120))
    


# from run import login

# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))