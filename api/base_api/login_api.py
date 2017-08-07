# -*- coding:utf-8 -*-
import json
import urllib

import requests

from  base_api import BaseApi
from image_captcha_api import ImageCaptchaApi
from utilities import db_operate


class LoginApi(BaseApi):
    """
    用户登录
    """
    url = '/login'

    def get_img_captcha(self, mobile):
        rep = ImageCaptchaApi(mobile=mobile).get()
        self.hash_key = json.loads(rep.content)['captcha_hash']
        captcha_code = db_operate.get_captcha(self.hash_key)
        return captcha_code

    def login(self, mobile, password):
        captcha_code = self.get_img_captcha(mobile)
        data = {
            "mobile": mobile,
            "password": password,
            "captcha_hash": self.hash_key,
            "captcha_code": captcha_code
        }

        self.response = requests.post(url=self.api_url(),
                                      data=data,
                                      headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        return self.response