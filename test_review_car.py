from base import BaseSeleniumTestCase
from pages.console.car_list_page import CarListPage
from pages.console.create_car_page import CreateCarPage
from pages.console.login_page import ConsoleLoginPage
from pages.console.to_do_task_page import ToDoTask
from settings import CAR_INFO, WAIT_FOR_REVIEW, BRAND, WAIT_FOR_RENT, REJECT
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import CONSOLE_USER_NAME, CONSOLE_PASSWORD


class ReviewCar(BaseSeleniumTestCase):

    def setUp(self):
        super(ReviewCar, self).setUp()
        db_operate.clean_car(BRAND)
        redis_helper.clean_redis()

    def create_car(self):
        ConsoleLoginPage(self.selenium).login(CONSOLE_USER_NAME, CONSOLE_PASSWORD)
        CreateCarPage(self.selenium).create_car()

    def test_pass_create_car(self):
        self.create_car()
        status = CarListPage(self.selenium).get_apply_car_status()
        self.assertEqual(status, WAIT_FOR_REVIEW)

        brand = CarListPage(self.selenium).get_apply_car_model()
        self.assertEqual(brand, CAR_INFO['brand'])

        ToDoTask(self.selenium).click_pass_btn()
        status = CarListPage(self.selenium).get_apply_car_status()
        self.assertEqual(status, WAIT_FOR_RENT)

        brand = CarListPage(self.selenium).get_apply_car_model()
        self.assertEqual(brand, CAR_INFO['brand'])

    def test_fail_create_car(self):
        self.create_car()
        status = CarListPage(self.selenium).get_apply_car_status()
        self.assertEqual(status, WAIT_FOR_REVIEW)

        brand = CarListPage(self.selenium).get_apply_car_model()
        self.assertEqual(brand, CAR_INFO['brand'])

        ToDoTask(self.selenium).click_fail_btn()
        status = CarListPage(self.selenium).get_apply_car_status()
        self.assertEqual(status, REJECT)

        brand = CarListPage(self.selenium).get_apply_car_model()
        self.assertEqual(brand, CAR_INFO['brand'])

    def tearDown(self):
        db_operate.clean_car(BRAND)
        redis_helper.clean_redis()
        super(ReviewCar, self).tearDown()


