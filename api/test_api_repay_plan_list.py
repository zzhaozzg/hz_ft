import json
from unittest import TestCase

from api.base_api.repay_plan_list_api import RepayPlanListApi
from api.settings import STATUS_CODE, COMPLETE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestRepayPlanListApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_completed_contract()
        redis_helper.clean_redis()

    def test_repay_plan_list_successful(self):
        rep_repay_list=RepayPlanListApi(USER_MOBILE, PASSWORD).post()
        self.assertEqual(rep_repay_list.status_code, STATUS_CODE)
        repay_list = (json.loads(rep_repay_list.content))['repaiedPlanList']
        self.assertEqual(len(repay_list), 12)
        self.assertEqual(repay_list[0]['status'], COMPLETE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()


