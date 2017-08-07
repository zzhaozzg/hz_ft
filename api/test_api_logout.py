import json
from unittest import TestCase

from api.base_api.logout_api import LogoutApi
from api.settings import STATUS_CODE, MESSAGE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestLogoutApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_logout_successful(self):
        rep = LogoutApi(USER_MOBILE, PASSWORD).get()
        self.assertEqual(rep.status_code, STATUS_CODE)
        message = json.loads(rep.content)['message']
        self.assertEqual(message, MESSAGE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()
