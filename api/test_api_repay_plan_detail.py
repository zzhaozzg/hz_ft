import json
from unittest import TestCase

from api.base_api.repay_plan_detail_api import RepayPlanDetailApi
from api.settings import STATUS_CODE, COMPLETE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestRepayPlanDetailApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_completed_contract()
        redis_helper.clean_redis()

    def test_repay_plan_detail(self):
        repay_id_list = InitUser().get_repay_id()
        rep_detail = RepayPlanDetailApi(USER_MOBILE, PASSWORD).post({'repayId': repay_id_list[0]['id']})
        self.assertEqual(rep_detail.status_code, STATUS_CODE)
        detail = json.loads(rep_detail.content)
        self.assertEqual(len(detail), 9)
        self.assertEqual(detail['status'], COMPLETE)
        self.assertEqual(detail['interest'], 82333)
        self.assertEqual(detail['overdueFee'], 0)
        self.assertEqual(detail['principal'], 416667)
        self.assertEqual(detail['repayDate'], '2016-01-01')

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()