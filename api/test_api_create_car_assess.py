from unittest import TestCase

from api.base_api.create_car_assess_api import CreateCarAssessApi
from api.settings import CAR_ASSESS, STATUS_CODE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestCreateCarAssessApi(TestCase):

    def setUp(self):
        db_operate.clean_contract(USER_MOBILE)
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user().create_contract()
        redis_helper.clean_redis()

    def test_create_car_access(self):
        rep = CreateCarAssessApi(USER_MOBILE, PASSWORD).post({"car_general": CAR_ASSESS['car_general'],
                                                                "car_brand": CAR_ASSESS['car_brand'],
                                                                "mileage": CAR_ASSESS['mileage'],
                                                                "city": CAR_ASSESS['city'],
                                                                "user_mobile": CAR_ASSESS['user_mobile'],
                                                                "car_series": CAR_ASSESS['car_series'],
                                                                "car_type": CAR_ASSESS['car_type'],
                                                                "car_bad": CAR_ASSESS['car_bad'],
                                                                "registration_time": CAR_ASSESS['registration_time'],
                                                                "car_good": CAR_ASSESS['car_good']
        })
        self.assertEqual(rep.status_code, STATUS_CODE)

    def tearDown(self):
        db_operate.clean_contract(USER_MOBILE)
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()