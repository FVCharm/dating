from flask import request, jsonify, current_app
import re

from app.api import bp
from app.forms.user import RegisterForm
from app.models.user import User
from app.models.base import db
from app.errors.error_code import Success, ClientTypeError, ParameterException
from app.api.auth import token_auth
from app.forms.edit import PersonalForm, LivelyForm

from app.utils.email import send_email


@bp.route('/register', methods=['POST'])
def create_user():
    '''注册一个新用户'''
    data = request.json
    form = RegisterForm(data=data)
    form.validate_for_api()
    User.register_by_phone(form.name.data,
                           form.phone.data,
                           form.password.data)
    return Success()


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    '''返回一个用户'''
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
def get_users():
    '''返回用户集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/personal/<int:id>', methods=['PUT'])
def update_personal(id):
    """ 修改一个用户 """
    data = request.json
    print(data)
    form = PersonalForm(data=data)
    user = User.query.get_or_404(id)
    form.validate_for_api()
    user.working_place = form.working_place.data
    user.username = form.username.data
    user.degree = form.degree.data
    user.height = form.height.data
    user.salary = form.salary.data
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/lively/<int:id>', methods=['PUT'])
def update_lively(id):
    """ 修改一个用户 """
    user = User.query.get_or_404(id)
    data = request.json
    form = LivelyForm(data=data)
    form.validate_for_api()
    user.marital_status = form.marital_status.data
    user.children = form.children.data
    user.house = form.house.data
    user.car = form.car.data
    user.smoke = form.smoke.data
    user.drink = form.drink.data
    user.health = form.health.data
    user.religion = form.religion.data
    db.session.commit()
    return jsonify(user.to_dict())


# @bp.route('/reset-password-request', methods=['POST'])
# def reset_password_request():
#     '''请求重置账户密码，需要提供注册时填写的邮箱地址'''
#     data = request.get_json()
#     if not data:
#         return ClientTypeError()
#
#     message = {}
#     if 'confirm_email_base_url' not in data or not data.get('confirm_email_base_url').strip():
#         message['confirm_email_base_url'] = 'Please provide a valid confirm email base url.'
#     pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
#     if 'email' not in data or not re.match(pattern, data.get('email', None)):
#         message['email'] = 'Please provide a valid email address.'
#     if message:
#         return ClientTypeError()
#
#     user = User.query.filter_by(phone=data.get('phone')).first()
#     if user:  # 如果提供的邮箱地址对应的用户实例对象存在，就发邮件
#         token = user.generate_reset_password_jwt()
#
#         text_body = '''
#         亲爱的 {0},
#         您好，需要重置密码请点击此链接: {1}
#         如果您不需要重置密码,请忽略此邮件。
#         您真诚的,
#         约会团队
#         注意: 不需要其他的回复.
#         '''.format(user.username, data.get('confirm_email_base_url') + token)
#
#         html_body = '''
#         <p>亲爱的 {0},</p>
#         <p>需要重置密码请 <a href="{1}">点击此处</a>。</p>
#         <p>如果您不需要重置密码,可忽略此邮件。</p>
#         <p>您真诚的，</p>
#         <p>约会团队</p>
#         <p><small>另外: 不需要回复此邮件。</small></p>
#         '''.format(user.username, data.get('confirm_email_base_url') + token)
#         print(data.get('email', None))
#
#         send_email('[dating] 重置密码',
#                    sender=current_app.config['MAIL_SENDER'],
#                    recipients=[data.get('email', None)],
#                    text_body=text_body,
#                    html_body=html_body)
#     # 不管前端提供的邮箱地址有没有对应的用户实例(不排除有人想恶意重置别人的账户)，都给他回应
#     return Success()


@bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    '''用户点击邮件中的链接，通过验证 JWT 来重置对应的账户的密码'''
    data = request.get_json()
    if not data:
        return ClientTypeError()
    if 'password' not in data or not data.get('password', None).strip():
        return ParameterException()
    user = User.query.filter_by(phone=data.get('phone')).first()
    if not user:
        return ParameterException()
    user.set_password(data.get('password'))
    db.session.commit()
    return Success()


@bp.route('/reset-pw', methods=['POST'])
def reset_pw():
    '''用户点击邮件中的链接，通过验证 JWT 来重置对应的账户的密码'''
    data = request.get_json()
    if not data:
        return ClientTypeError()
    user = User.query.filter_by(phone=data.get('phone')).first()
    print(data.get('phone'))
    if not user:
        return ParameterException()
    user.set_password(data.get('password'))
    db.session.commit()
    return Success()


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    '''删除一个用户'''
    pass
