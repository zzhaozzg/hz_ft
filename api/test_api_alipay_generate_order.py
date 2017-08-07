import json
from unittest import TestCase

from api.base_api.alipay_generate_order_api import AlipayGenerateOrderApi
from api.settings import STATUS_CODE
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities.set_up import InitUser


class  TestAlipayGenerateOrder(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        InitUser().create_new_user().create_contract()
        redis_helper.clean_redis()

    def test_alipay_generate_order_ios(self):
        repay_id_list = InitUser().get_repay_id()
        rep = AlipayGenerateOrderApi(USER_MOBILE, PASSWORD).post({'bid': repay_id_list[0]['id'],
                                                                  'fee_type': 'REPAY_PLAN_FEE',})
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_content = json.loads(rep.content)
        self.assertEqual(rep_content['total_fee'], 503990)

    def test_alipay_generate_order_android(self):
        repay_id_list = InitUser().get_repay_id()
        AlipayGenerateOrderApi(USER_MOBILE,PASSWORD).platform = 'Android'
        rep = AlipayGenerateOrderApi(USER_MOBILE, PASSWORD).post({'bid': repay_id_list[0]['id'],
                                                                  'fee_type': 'REPAY_PLAN_FEE', })
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_content = json.loads(rep.content)
        self.assertEqual(rep_content['total_fee'], 503990)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()