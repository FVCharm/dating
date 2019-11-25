from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, current_app
import jwt
from datetime import datetime, timedelta

from app.models.base import Base, db


class PaginatedAPIMixin(object):
    pass


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(24), unique=True, nullable=False)
    _password = db.Column('password', db.String(128))

    name = db.Column('name', db.String(12))

    def __repr__(self):
        return '<User {}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def to_dict(self, include_phone=False):
        data = {
            'id': self.id,
            'name': self.name,
            '_links': {
                'self': url_for('api.get_user', id=self.id)
            }
        }
        if include_phone:
            data['phone'] = self.phone
        return data

    @staticmethod
    def register_by_phone(name, phone, password):
        with db.auto_commit():
            user = User()
            user.name = name
            user.phone = phone
            user.password = password
            db.session.add(user)

    def get_jwt(self, expires_in=600):
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'name': self.name if self.name else self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidSignatureError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return None
        return User.query.get(payload.get('user_id'))







