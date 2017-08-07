import json
from unittest import TestCase

from api.base_api.verify_sms_code_api import VerifySmsCodeApi
from utilities import redis_helper
from utilities import db_operate
from utilities.fake_user import USER_MOBILE
from settings import STATUS_CODE, MESSAGE, VERIFY_CODE, FAIL_STATUS_CODE, ERROR_SMS_MESSAGE


class TestVerifySmsCodeApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

    def test_sms_code_successful(self):
        verify_code = VerifySmsCodeApi().get_sms_captcha()
        rep = VerifySmsCodeApi().post({'mobile': USER_MOBILE,
                                       'verify_code': verify_code})
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_message = json.loads(rep.content)['message']
        self.assertEqual(rep_message, MESSAGE)

    def test_sms_code_failed(self):
        rep = VerifySmsCodeApi().post({'mobile': USER_MOBILE,
                                       'verify_code': VERIFY_CODE})
        self.assertEqual(rep.status_code, FAIL_STATUS_CODE)
        rep_message = json.loads(rep.content)['message']
        self.assertEqual(rep_message, ERROR_SMS_MESSAGE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()