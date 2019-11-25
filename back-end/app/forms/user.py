from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange
from wtforms import ValidationError

from app.models.user import User
from app.forms.base import BaseForm


class RegisterForm(BaseForm):
    name = StringField('昵称', validators=[DataRequired(message='昵称不能为空'), Length(2, 10, message='昵称长度为2~10个字符')])
    phone = IntegerField('手机号', validators=[
        DataRequired(message='不允许为空'),
        NumberRange(min=10000000000, max=99999999999)])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不能为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,20}$', message='密码必须为6~20位的大小写字母或数字')])

    def validate_phone(self, field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('该手机号已注册，请直接登录')


class LoginForm(BaseForm):
    phone = IntegerField('手机号', validators=[
        DataRequired(message='不允许为空'),
        NumberRange(min=10000000000, max=99999999999)])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不能为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,20}$', message='密码必须为6~20位的大小写字母或数字')])