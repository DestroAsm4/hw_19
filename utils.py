import jwt
from flask import request
from flask_restx import abort

from constants import JWT_ALGORITHM, JWT_SECRET


def auth_require(func):

    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer')[-1].strip()

        try:
            jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper

print(auth_require)

def admin_require(func):

    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer')[-1].strip()

        try:
            user = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
            if user['role'] != 'admin':
                abort(401)
        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)
            return func(*args, **kwargs)
    return wrapper