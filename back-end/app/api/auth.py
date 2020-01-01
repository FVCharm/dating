from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models.user import User
from app.errors.error_code import AuthFailed

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(phone, password):
    user = User.query.filter_by(phone=phone).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    return AuthFailed()


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.verify_jwt(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    '''用于在 Token Auth 认证失败的情况下返回错误响应'''
    return AuthFailed()


