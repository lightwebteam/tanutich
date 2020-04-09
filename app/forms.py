from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class Registr(FlaskForm):
    username = StringField('Введите имя', validators=[DataRequired()])
    password = PasswordField('Введите Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')