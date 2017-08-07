from base import BaseSeleniumTestCase
from pages.console.create_contract_page import CreateContractPage
from pages.console.login_page import ConsoleLoginPage
from utilities import db_operate
from utilities import redis_helper
from utilities.fake_user import USER_MOBILE, CONSOLE_USER_NAME, CONSOLE_PASSWORD


class TestCreateContract(BaseSeleniumTestCase):

    def setUp(self):
        super(TestCreateContract, self).setUp()
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()

    def test_create_contract_successful(self):
        ConsoleLoginPage(self.selenium).login(CONSOLE_USER_NAME, CONSOLE_PASSWORD)
        CreateContractPage(self.selenium).create_contract().approve_contract()

    def tearDown(self):
        db_operate.clean_user(USER_MOBILE)
        db_operate.clean_contract(USER_MOBILE)
        redis_helper.clean_redis()
        super(TestCreateContract, self).tearDown()