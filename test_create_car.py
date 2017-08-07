# -*- coding:utf-8 -*-
from base import BaseSeleniumTestCase
from pages.console.car_list_page import CarListPage
from pages.console.login_page import ConsoleLoginPage
from settings import CAR_INFO, BRAND, WAIT_FOR_REVIEW
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import CONSOLE_USER_NAME, CONSOLE_PASSWORD, USER_MOBILE
from pages.console.create_car_page import  CreateCarPage


class TestCreateCar(BaseSeleniumTestCase):

    def setUp(self):
        super(TestCreateCar, self).setUp()
        db_operate.clean_contract(USER_MOBILE)
        db_operate.clean_car(BRAND)
        redis_helper.clean_redis()

    def test_create_car_successful(self):
        ConsoleLoginPage(self.selenium).login(CONSOLE_USER_NAME, CONSOLE_PASSWORD)
        CreateCarPage(self.selenium).create_car()
        status = CarListPage(self.selenium).get_apply_car_status()
        self.assertEqual(status, WAIT_FOR_REVIEW)

        brand = CarListPage(self.selenium).get_apply_car_model()
        self.assertEqual(brand, CAR_INFO['brand'])

    def tearDown(self):
        db_operate.clean_car(BRAND)
        redis_helper.clean_redis()
        super(TestCreateCar, self).tearDown()