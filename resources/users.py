import models

from flask import request, jsonify, Blueprint, redirect, g 
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/', methods=["GET"])
def test():
    return 'route working'

@user.route('/register', methods=["POST"])
def register():
    payload = request.get_json()
    payload['username'] = payload['username'].lower()
    payload['email'] = payload['email'].lower()
 
    try:
        models.User.get(models.User.email == payload['email']) 
        return jsonify(data={}, status={"code": 401, "message": "Username/Email already exists"})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password']) 
        user = models.User.create(**payload) 
        login_user(user)

        currentUser = model_to_dict(current_user)
        del currentUser['email']
        del currentUser['password']
        
        user_dict = model_to_dict(user)
        del user_dict['password']
        return jsonify(data=user_dict, status={"code": 201, "message": "Success"}, session=currentUser)

@user.route('/login', methods=["GET","POST"])
def login():
    payload = request.get_json()

    try:
        user = models.User.get(models.User.username == payload['username'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)

            currentUser = model_to_dict(current_user)
            del currentUser['email']
            del currentUser['password']

            return jsonify(data=user_dict, status={"code": 200, "message": "Success"}, session=currentUser)
        else:
            return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})


@user.route('/logout')
def logout():
    logout_user()
    return jsonify(data={}, status={"code": 202, "message": "logged out success"})
