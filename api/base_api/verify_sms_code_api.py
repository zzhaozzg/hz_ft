# -*- coding:utf-8 -*-
import session
from api.base_api.base_api import BaseApi


class VerifySmsCodeApi(BaseApi):
    """
    验证短信验证码
    """
    url = '/verify-sms-code'

    def get_sms_captcha(self):
        return session.get_sms_captcha(mobile=self.mobile)

    def build_custom_param(self, data):
        return {
            "mobile": data['mobile'],
            "verify_code": data['verify_code']
        }