import time

from pages.base_page import BaseConsolePage


class ConsoleLoginPage(BaseConsolePage):

    url = '/login'

    def login_name(self, username):
        self.find_element_by_id("username").send_keys(username)
        return self

    def pass_word(self, password):
        self.find_element_by_id("password").send_keys(password)
        return self

    def click_login_btn(self):
        self.find_element_by_css('.btn').click()
        return self

    def login(self, username, password):
        self.login_name(username).pass_word(password).click_login_btn()
        time.sleep(5)
        return self