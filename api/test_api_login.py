# -*- coding:utf-8 -*-
import json
from unittest import TestCase
from api.base_api.login_api import LoginApi
from utilities.fake_user import USER_MOBILE, PASSWORD
from utilities import redis_helper,db_operate
from utilities.set_up import InitUser
from settings import STATUS_CODE, ERROR_MOB_OR_PWD


class TestLoginApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_login_successful(self):
        rep = LoginApi().login(USER_MOBILE, PASSWORD)
        self.assertEqual(rep.status_code, STATUS_CODE)
        token = json.loads(rep.content)['token']
        self.assertEqual(len(token), 36)

    def test_login_failed(self):
        rep = LoginApi().login(USER_MOBILE, PASSWORD + '01')
        self.assertEqual(rep.status_code, 401)
        message = json.loads(rep.content)['message']
        self.assertEqual(message, ERROR_MOB_OR_PWD)

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

