from app import tanutich
from app.forms import Registr
from flask import request, redirect, render_template, jsonify, json
from flask_login import login_required
from app.models import User
from app import db

@tanutich.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@tanutich.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        return jsonify(status='success')
    return render_template('login.html')

@tanutich.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        print(username, password, repeat_password)

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

        print(json_answer)
        # user = User(id=user_id, username=username, password=password)
        # db.session.add(user)
        # db.session.commit()

        return json.dumps(json_answer)
    return render_template('register.html')