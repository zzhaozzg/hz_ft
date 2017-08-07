import json
from unittest import TestCase

from api.base_api.my_fund_api import MyFundApi
from api.settings import STATUS_CODE, COMPLETE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestMyFundApi(TestCase):
    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_completed_contract()
        redis_helper.clean_redis()

    def test_my_fund(self):
        rep = MyFundApi(USER_MOBILE, PASSWORD).post()
        my_fund = json.loads(rep.content)
        self.assertEqual(rep.status_code, STATUS_CODE)
        self.assertEqual(len(my_fund), 9)
        self.assertEqual(my_fund['annualRate'], 2.0)
        insurance_list = my_fund['insuranceList'][0]
        self.assertEqual(len(insurance_list), 6)
        self.assertEqual(insurance_list['tradeTime'], '2016-01-06')
        self.assertEqual(insurance_list['status'], COMPLETE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()