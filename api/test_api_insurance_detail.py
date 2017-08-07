import json
from unittest import TestCase

from api.base_api.insurance_detail_api import InsuranceDetailApi
from api.settings import STATUS_CODE, COMPLETE, REPAYDATE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestInsuranceDetailApi(TestCase):
    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_completed_contract()
        redis_helper.clean_redis()

    def test_insurance_detail(self):
        insurance_id = InitUser().get_insurance_id()
        rep = InsuranceDetailApi(USER_MOBILE, PASSWORD).post({'bid': insurance_id})
        self.assertEqual(rep.status_code, STATUS_CODE)
        detail = json.loads(rep.content)
        self.assertEqual(len(detail), 7)
        self.assertEqual(detail['status'], COMPLETE)
        self.assertEqual(detail['repayDate'], REPAYDATE)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()