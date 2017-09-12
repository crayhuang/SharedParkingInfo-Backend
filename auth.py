#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib
from flask_api.exceptions import APIException

APP_ID = "APPID12345"
APP_SECRET = "APPSECRET12345"

def check_sign_api(args):
    """
    :param args: 需要认证的参数
    :return 是否签名通过
    """
    timestamp = str(args.get('timestamp'))
    signature = args.get('sign')
    m = hashlib.sha1()
    encrypted_str = ''.join([timestamp, APP_ID, APP_SECRET])
    m.update(encrypted_str.encode('utf-8'))
    print(m.hexdigest())
    if signature != m.hexdigest():
        raise AuthenticationFailed()
    
    return True

class AuthenticationFailed(APIException):
    status_code = 401
    detail = "401 Unauthenticated"