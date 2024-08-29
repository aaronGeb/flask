#!/usr/bin/env python3
from flask import Flask
from flask import request, response, render_template, redirect
from repository.user import validate_user


app = Flask(__name__)


@app.route('/login/params')
def login_with_params():
    username = request.args['username']
    password = request.args['password']
    if validate_user(username, password):
        return 'Login successful'
    else:
        return 'Login failed'
