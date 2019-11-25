from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
import os
import base64
from datetime import datetime, timedelta

from app.models.base import Base, db


class PaginatedAPIMixin(object):
    pass


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(24), unique=True, nullable=False)
    _password = db.Column('password', db.String(128))

    name = db.Column('name', db.String(12))

    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

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

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user





