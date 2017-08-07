# -*- coding:utf-8 -*-
import json
from unittest import TestCase

from api.settings import STATUS_CODE, OLD_PWD_ERROR
from utilities import db_operate, redis_helper
from utilities.fake_user import USER_MOBILE, PASSWORD, NEW_PASSWORD
from utilities.set_up import InitUser
from base_api.modify_password_api import ModifyPassWordApi
from base_api.login_api import LoginApi


class TestModifyPassWordApi(TestCase):

    def setUp(self):
        db_operate.clean_user(USER_MOBILE)
        InitUser().create_new_user()
        redis_helper.clean_redis()

    def test_modify_password_successful(self):
        rep_modify = ModifyPassWordApi(USER_MOBILE, PASSWORD).post({"oldPassword": PASSWORD,
                                                                    "password": NEW_PASSWORD})
        self.assertEqual(rep_modify.status_code, STATUS_CODE)
        message = json.loads(rep_modify.content)['message']
        self.assertEqual(message, '')
        rep = LoginApi().login(USER_MOBILE, NEW_PASSWORD)
        token = json.loads(rep.content)['token']
        self.assertEqual(len(token), 36)

    def test_modify_password_failed(self):
        rep_modify = ModifyPassWordApi(USER_MOBILE, PASSWORD).post({"oldPassword": NEW_PASSWORD,
                                                                    "password": PASSWORD})
        message = json.loads(rep_modify.content)['message']
        self.assertEqual(message, OLD_PWD_ERROR)


    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        redis_helper.clean_redis()

