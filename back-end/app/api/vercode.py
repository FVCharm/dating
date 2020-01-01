from flask import jsonify, request

from app.api import bp
from app.utils.send_msg import send_message
from app.forms.verify import VerifyForm
from app.errors.error_code import Success


@bp.route('/verify', methods=['POST'])
def send_msg():
    '''注册一个新用户'''
    data = request.json
    form = VerifyForm(data=data)
    form.validate_for_api()
    response = send_message(form.phone.data)

    return response

