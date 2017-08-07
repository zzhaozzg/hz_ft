import json
from unittest import TestCase

from api.base_api.my_car_api import MyCarApi
from api.settings import STATUS_CODE, PLATENUMBER
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestMyCarApi(TestCase):
    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_contract()
        redis_helper.clean_redis()

    def test_my_car_successful(self):
        rep = MyCarApi(USER_MOBILE, PASSWORD).post()
        self.assertEqual(rep.status_code,STATUS_CODE)
        rep_content = json.loads(rep.content)
        self.assertEqual(len(rep_content), 8)
        self.assertEqual(rep_content['plateNumber'], PLATENUMBER)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()
