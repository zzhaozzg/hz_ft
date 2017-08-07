import json
from unittest import TestCase

from api.base_api.index_api import IndexApi
from api.settings import STATUS_CODE, GENERATE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class TestIndexApi(TestCase):
    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_contract()
        redis_helper.clean_redis()

    def test_index(self):
        rep = IndexApi(USER_MOBILE, PASSWORD).post()
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_content = json.loads(rep.content)
        self.assertEqual(len(rep_content),11)
        self.assertEqual(len(rep_content['currentInsurance']), 7)
        self.assertEqual(rep_content['status'], GENERATE)
        self.assertEqual(rep_content['currentLoanAmount'], 80000000)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()