from flask import jsonify, request

from app.api import bp
from app.utils.send_msg import send_message
from app.forms.verify import VerifyForm
from app.errors.error_code import Success, ClientTypeError, ParameterException
from app.models.user import User


@bp.route('/verify', methods=['POST'])
def send_msg():
    '''发送邮件'''
    data = request.json
    form = VerifyForm(data=data)
    form.validate_for_api()
    response = send_message(form.phone.data)

    return response


@bp.route('/send-code', methods=['POST'])
def send_code():
    '''请求重置账户密码，需要提供注册时填写的邮箱地址'''
    data = request.get_json()
    if not data:
        return ClientTypeError()
    form = VerifyForm(data=data)
    form.validate_for_api()
    user = User.query.filter_by(phone=form.phone.data).first()
    if user:  # 如果提供的邮箱地址对应的用户实例对象存在，就发邮件
        response = send_message(form.phone.data)
        return response
    else:
        return ClientTypeError()




