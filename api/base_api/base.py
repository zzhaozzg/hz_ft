import logging
from unittest import TestCase
from selenium import webdriver
import settings


logger = logging.getLogger(__name__)


class BaseSeleniumTestCase(TestCase):

    def get_web_driver(self):
        driver = webdriver.Firefox(executable_path=settings.GECKODRIVER_PATH) if settings.ENV == 'dev' \
            else webdriver.PhantomJS()
        driver.set_window_size(1400, 1000)
        return driver

    def setUp(self):
        self.selenium = self.get_web_driver()

    def tearDown(self):
        self.selenium.quit()