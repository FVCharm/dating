from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, current_app
import jwt
from datetime import datetime, timedelta
from hashlib import md5

from app.models.base import Base, db


class PaginatedAPIMixin(object):
    pass


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(24), unique=True, nullable=False)
    _password = db.Column('password', db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    name = db.Column('姓名', db.String(12))
    ethnic_group = db.Column('民族', db.String(12))
    birthday = db.Column('生日', db.String(12))
    native_place = db.Column('籍贯', db.String(12))

    # personalForm
    username = db.Column('username', db.String(12))
    working_place = db.Column('工作地点', db.String(32))
    salary = db.Column('月薪', db.String, default=0)
    degree = db.Column('学历', db.String, default=0)
    height = db.Column('身高', db.String, default=170)
    gender = db.Column('性别', db.String, default=0)
    occupation = db.Column('职业', db.String, default=0)

    # contactForm
    qq = db.Column('QQ', db.String(24), unique=True)
    weixin = db.Column('微信', db.String(48), unique=True)

    # livelyForm
    marital_status = db.Column('婚姻状况', db.String, default=0)
    children = db.Column('小孩', db.String, default=0)
    house = db.Column('房', db.String, default=0)
    car = db.Column('车', db.String, default=0)
    drink = db.Column('喝酒', db.String, default=0)
    smoke = db.Column('吸烟', db.String, default=0)
    health = db.Column('健康状况', db.String, default=0)
    religion = db.Column('宗教信仰', db.String, default=0)

    # hobbyForm
    topic = db.Column('兴趣话题', db.String, default=0)
    sport = db.Column('体育运动', db.String, default=0)
    ball = db.Column('球类运动', db.String, default=0)
    leisure = db.Column('休闲娱乐', db.String, default=0)
    dietary = db.Column('饮食偏好', db.String, default=0)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    @property
    def password(self):
        return self._password

    def generate_confirm_jwt(self, expires_in=3600):
        '''生成确认账户的 JWT'''
        now = datetime.utcnow()
        payload = {
            'confirm': self.id,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    def verify_confirm_jwt(self, token):
        '''用户点击确认邮件中的URL后，需要检验 JWT，如果检验通过，则把新添加的 confirmed 属性设为 True'''
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return False
        if payload.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self, include_phone=False):
        data = {
            'id': self.id,
            'name': self.username,
            'phone': self.phone,
            '_links': {
                'self': url_for('api.get_user', id=self.id)
            },
            'personalForm': {
                'username': self.username,
                'working_place': self.working_place,
                'salary': self.salary,
                'degree': self.degree,
                'height': self.height,
                'occupation': self.occupation
            },
            'livelyForm': {
                'status': self.marital_status,
                'children': self.children,
                'house': self.house,
                'car': self.car,
                'drink': self.drink,
                'smoke': self.smoke,
                'health': self.health,
                'religion': self.religion
            }
        }
        if include_phone:
            data['phone'] = self.phone
        return data

    @staticmethod
    def register_by_phone(name, phone, password):
        with db.auto_commit():
            user = User()
            user.username = name
            user.phone = phone
            user.password = password
            db.session.add(user)

    def get_jwt(self, expires_in=600):
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'name': self.username if self.username else self.name,
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

    def avatar(self, size):
        digest = md5(self.phone.encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def generate_reset_password_jwt(self, expires_in=3600):
        '''生成重置账户密码的 JWT'''
        now = datetime.utcnow()
        payload = {
            'reset_password': self.id,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_jwt(token):
        '''用户点击重置密码邮件中的URL后，需要检验 JWT
        如果检验通过，则返回 JWT 中存储的 id 所对应的用户实例'''
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return None
        return User.query.get(payload.get('reset_password'))



