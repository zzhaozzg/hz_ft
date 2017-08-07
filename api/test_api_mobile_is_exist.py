import json
from unittest import TestCase

from api.base_api.mobile_is_exist_api import MobileIsExistApi
from utilities import redis_helper
from utilities import db_operate
from utilities.fake_user import USER_MOBILE, NEW_USER_MOBILE
from utilities.set_up import InitUser
from settings import STATUS_CODE, REGISTERED, NOT_REGISTERED


class TestMobileIsExistApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_mobile_is_exist(self):
        rep = MobileIsExistApi().post({'mobile': USER_MOBILE})
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_registered = json.loads(rep.content)['registered']
        self.assertEqual(rep_registered, REGISTERED)

    def test_mobile_is_not_exist(self):
        rep = MobileIsExistApi().post({'mobile': NEW_USER_MOBILE})
        self.assertEqual(rep.status_code, STATUS_CODE)
        registered = json.loads(rep.content)['registered']
        self.assertEqual(registered, NOT_REGISTERED)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()
