# -*- coding:utf-8 -*-
import json
import user


from api.base_api.base_api import BaseApi
from api.base_api.image_captcha_api import ImageCaptchaApi
from utilities import db_operate
import session

class RegisterApi(BaseApi):
    """
    用户注册
    """
    url = '/register'

    def get_sms_captcha(self):
        return session.get_sms_captcha(mobile=self.mobile)

    def build_custom_param(self, data):
        return{
            "verify_code": data['verify_code'],
            "mobile": data['mobile'],
            "password": data['password'],
        }






