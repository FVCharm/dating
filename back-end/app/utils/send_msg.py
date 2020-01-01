from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from random import randint
from flask import json, jsonify
import os

from app.errors.error_code import PhoneError, BusinessLimit, ServerError


access_key_id = os.getenv('ACCESS_KEY_ID', '<accessKeyId>')
access_secret = os.getenv('ACCESS_KEY_SECRET', '<accessSecret>')


def send_message(phone):
    client = AcsClient(access_key_id, access_secret, 'default')

    code = randint(100000, 999999)

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "default")
    request.add_query_param('PhoneNumbers', '{}'.format(phone))
    request.add_query_param('SignName', "寻觅")
    request.add_query_param('TemplateCode', "SMS_172880009")
    request.add_query_param('TemplateParam', '{{"code":"{}"}}'.format(code))

    response = client.do_action(request)
    resp = conversion_resp(response, code)
    return resp


def conversion_resp(r, code):
    response = json.loads(str(r, encoding='utf-8'))
    if response['Message'] == 'OK' and response['Code'] == 'OK':
        response = jsonify({'code': code, 'error_code': 0})
    elif response['Code'] == "isv.MOBILE_NUMBER_ILLEGAL":
        response = PhoneError()
    elif response['Code'] == 'isv.BUSINESS_LIMIT_CONTROL' or response['Code'] == 'DOMESTIC_NUMBER_NOT_SUPPORTED':
        response = BusinessLimit()
    else:
        response = ServerError()

    return response
