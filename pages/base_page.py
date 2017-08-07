import logging
import os
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

import settings
from settings import WAIT_TIME

logger = logging.getLogger(__name__)


def fail_on_screenshot(function):
    def get_snapshot_directory():
        if not os.path.exists(settings.SNAPSHOT_DIRECTORY):
            os.mkdir(settings.SNAPSHOT_DIRECTORY)
        return settings.SNAPSHOT_DIRECTORY

    def get_current_time_str():
        return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")

    def wrapper(*args, **kwargs):
        instance, selector = args[0], args[1]
        try:
            return function(*args, **kwargs)
        except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
            logger.error("Could not find the selector: [{}].".format(selector))
            filename = "{}.png".format(get_current_time_str())
            screenshot_path = os.path.join(get_snapshot_directory(), filename)
            logger.debug(instance.selenium.page_source)
            instance.selenium.save_screenshot(screenshot_path)
            raise ex

    return wrapper


class BasePage(object):
    url = ""
    base_url = ""

    def __init__(self, selenium, url_params=()):
        self.selenium = selenium
        self.url_params = url_params if url_params else []
        self.__go_to()

    def __go_to(self):
        logger.debug("Go to page: [{}]".format(self.get_page_url()))
        return self._selenium_get_url(self.get_page_url())

    def refresh(self):
        self.selenium.refresh()

    def navigate_back(self):
        self.selenium.back()

    def _selenium_get_url(self, url):
        try:
            self.selenium.get('about:blank')
            self.selenium.get(str(url))
        except Exception as ex:
            logger.error("Can not open the url:[{}]".format(url))
            raise ex
        return self

    def get_page_url(self):
        if not self.url:
            raise RuntimeError("no url been set")
        return self._get_url(self.url)

    def _get_url(self, url):
        format_url = url.format(*self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    def get_current_page_url(self):
        return self.selenium.current_url

    def execute_js(self, js):
        return self.selenium.execute_script(js)

    @fail_on_screenshot
    def find_element_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_elements_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_elements_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def find_element_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def find_element_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def find_elements_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.XPATH, selector)))

    @fail_on_screenshot
    def invisible_element_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def invisible_element_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def invisible_element_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def invisible_element_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_sub_element_by_css(self, selector, elem):
        return elem.find_element(By.CSS_SELECTOR, selector)

    @fail_on_screenshot
    def find_sub_elements_by_css(self, selector, elem):
        return elem.find_elements(By.CSS_SELECTOR, selector)

    @fail_on_screenshot
    def find_sub_elements_by_xpath(self, selector, elem):
        return elem.find_elements(By.XPATH, selector)

    @fail_on_screenshot
    def find_sub_element_by_xpath(self, selector, elem):
        return elem.find_element(By.XPATH, selector)

    @fail_on_screenshot
    def find_sub_element_by_tag(self, selector, elem):
        return elem.find_element(By.TAG_NAME, selector)



class BaseConsolePage(BasePage):
    base_url = settings.CONSOLE_TEST_BASE_URL


