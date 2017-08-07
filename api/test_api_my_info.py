import json
from unittest import TestCase

from api.base_api.my_info_api import MyInfoApi
from api.settings import STATUS_CODE, NONE, MALE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import PASSWORD, USER_MOBILE
from utilities.set_up import InitUser


class TestMyInfoApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_my_info_not_user_profile(self):
        rep = MyInfoApi(USER_MOBILE, PASSWORD).post()
        self.assertEqual(rep.status_code, STATUS_CODE)
        content = json.loads(rep.content)
        self.assertEqual(USER_MOBILE, content['mobile'])
        self.assertEqual(NONE, content['carStatus'])
        self.assertEqual(u'', content['realName'])

    def test_my_info(self):
        InitUser().create_completed_contract()
        rep = MyInfoApi(USER_MOBILE, PASSWORD).post()
        self.assertEqual(rep.status_code, STATUS_CODE)
        content = json.loads(rep.content)
        self.assertEqual(USER_MOBILE, content['mobile'])
        self.assertEqual(MALE, content['gender'])
        self.assertEqual(NONE, content['carStatus'])

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()