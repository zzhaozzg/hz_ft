# -*- coding:utf-8 -*-
import json
from unittest import TestCase

from api.base_api.find_password_api import FindPassWordApi
from api.base_api.send_verify_code_api import SendVerifyCodeApi
from api.base_api.verify_sms_code_api import VerifySmsCodeApi

from utilities import redis_helper
from utilities import db_operate
from utilities.fake_user import USER_MOBILE, NEW_PASSWORD
from utilities.set_up import InitUser
from api.settings import STATUS_CODE, MESSAGE


class TestFindPassWordApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_find_password_successful(self):
        get_list = SendVerifyCodeApi().get_img_captcha()
        captcha_code = get_list[0]
        captcha_hash = get_list[1]
        send_sms_response = SendVerifyCodeApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                                 'captcha_code': captcha_code,
                                                                 'captcha_hash': captcha_hash
                                                                 })
        self.assertEqual(send_sms_response.status_code, STATUS_CODE)
        rep_message = json.loads(send_sms_response.content)['message']
        self.assertEqual(MESSAGE, rep_message)

        verify_code = VerifySmsCodeApi().get_sms_captcha()
        rep_verify = VerifySmsCodeApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                         'verify_code': verify_code})
        self.assertEqual(rep_verify.status_code, STATUS_CODE)

        rep_find = FindPassWordApi(mobile=USER_MOBILE).post({"mobile": USER_MOBILE,
                                                             "password": NEW_PASSWORD})
        message = json.loads(rep_find.text)['message']
        self.assertEqual(rep_find.status_code, STATUS_CODE)
        self.assertEqual(u'', message)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

