import json
from unittest import TestCase

from api.base_api.send_verify_code_api import SendVerifyCodeApi
from api.settings import MESSAGE, ERROR_IMG_MESSAGE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE


class TestSendSmsCodeApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

    def test_send_sms_code_successful(self):
        get_list = SendVerifyCodeApi().get_img_captcha()
        captcha_code = get_list[0]
        captcha_hash = get_list[1]
        send_sms_response = SendVerifyCodeApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                                 'captcha_code': captcha_code,
                                                                 'captcha_hash': captcha_hash})
        rep_message = json.loads(send_sms_response.content)['message']
        self.assertEqual(MESSAGE, rep_message)

    def test_send_sms_code_fail(self):
        get_list = SendVerifyCodeApi().get_img_captcha()
        captcha_code = get_list[0]
        captcha_hash = get_list[1]
        send_sms_response = SendVerifyCodeApi(USER_MOBILE).post({'mobile': USER_MOBILE,
                                                                 'captcha_code': str(captcha_code)+'1',
                                                                 'captcha_hash': captcha_hash})
        rep_message = json.loads(send_sms_response.content)['message']
        self.assertEqual(ERROR_IMG_MESSAGE, rep_message)

