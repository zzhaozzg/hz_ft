# -*- coding:utf-8 -*-
import session
from api.base_api.base_api import BaseApi


class FindPassWordApi(BaseApi):
    """
    找回密码
    """
    url = '/find-password'

    def get_sms_captcha(self):
        return session.get_sms_captcha(mobile=self.mobile)

    def build_custom_param(self, data):
        verify_code = self.get_sms_captcha()
        return {
            "verify_code": verify_code,
            "mobile": data['mobile'],
            "password": data['password'],
        }
