# -*- coding:utf-8 -*-
import json

from api.base_api.base_api import BaseApi
from api.base_api.image_captcha_api import ImageCaptchaApi
from utilities import db_operate


class SendVerifyCodeApi(BaseApi):
    """
    发送短信验证码
    """
    url = '/send-verify-code'

    def get_img_captcha(self):
        response = ImageCaptchaApi(mobile=self.mobile).get()
        hash_key = json.loads(response.content)['captcha_hash']
        captcha_code = db_operate.get_captcha(hash_key)
        return [captcha_code, hash_key]

    def build_custom_param(self, data):
        return {
            "mobile": data['mobile'],
            "captcha_code": data['captcha_code'],
            "captcha_hash": data['captcha_hash']
        }