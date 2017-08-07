# -*- coding=utf-8 -*-
import json
from unittest import  TestCase

from base_api.register_api import  RegisterApi
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities import db_operate
from utilities import  redis_helper
from settings import STATUS_CODE, FAIL_STATUS_CODE, ERROR_SMS_MESSAGE



class TestRegisterApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

    def test_register_successful(self):
        verify_code = RegisterApi().get_sms_captcha()
        rep = RegisterApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                      'password': PASSWORD,
                                                      'verify_code': verify_code})
        self.assertEqual(rep.status_code, STATUS_CODE)
        token = json.loads(rep.content)['token']
        self.assertEqual(len(token), 36)

    def test_register_fail_sms_error(self):
        verify_code = RegisterApi().get_sms_captcha()
        rep = RegisterApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                      'password': PASSWORD,
                                                      'verify_code': str(verify_code) + '1'})
        self.assertEqual(rep.status_code, FAIL_STATUS_CODE)
        rep_message = json.loads(rep.content)['message']
        self.assertEqual(rep_message, ERROR_SMS_MESSAGE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()


