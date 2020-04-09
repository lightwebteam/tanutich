from app import tanutich
from app.forms import Registr
from flask import request, redirect, render_template, jsonify, json
# from flask_login import login_required
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


@tanutich.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@tanutich.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query_user = User.query.filter(User.username == username).first()
        if query_user is not None:
            query_password = User.query.filter(User.username == username).with_entities(User.password).first()[0]
            if check_password_hash(query_password, password):
                print('Логин')
        return jsonify(status='success')
    return render_template('login.html')

@tanutich.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        validate_username = User.query.filter(User.username == username).first()

        json_answer = {
            'username': [],
            'password': []
        }

        if validate_username is not None:
            json_answer['username'].append('dublicate_username')
        if len(password) < 6:
            json_answer['password'].append('short_password')
        if password != repeat_password:
            json_answer['password'].append('wrong_repeat_password')

        max_id = db.session.query(db.func.max(User.id)).first()[0]

        if max_id is None:
            user_id = 1
        else:
            user_id = max_id + 1

        if len(json_answer['username']) == 0 and len(json_answer['password']) == 0:
            user = User(id=user_id, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

        return json.dumps(json_answer)
    return render_template('register.html')