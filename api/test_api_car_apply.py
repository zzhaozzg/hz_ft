import json
from unittest import TestCase

from api.base_api.car_apply_api import  CarApplyApi
from utilities import redis_helper
from utilities import db_operate
from utilities.fake_user import USER_MOBILE, PASSWORD
from api.settings import CAR_BRAND, CAR_PRICE, STATUS_CODE
from utilities.set_up import InitUser


class TestCarApplyApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_car_apply_successful(self):
        rep_car = CarApplyApi(USER_MOBILE, PASSWORD).post({'car_brand': CAR_BRAND,'car_price':CAR_PRICE})
        self.assertEqual(rep_car.status_code, STATUS_CODE)
        message = json.loads(rep_car.content)['message']
        self.assertEqual(u'', message)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()
