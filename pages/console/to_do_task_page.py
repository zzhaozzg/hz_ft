# -*- coding:utf-8 -*-
import time

from pages.base_page import BaseConsolePage


class ToDoTask(BaseConsolePage):

    url = ' '

    def _go_to_page(self):
        self.find_element_by_link_text('待办任务').click()
        time.sleep(5)

    def _go_to_task_page(self):
        return self._go_to_page()

    def _click_pass_btn(self):
        return self.find_element_by_id('approve').click()

    def _click_fail_btn(self):
        return self.find_element_by_id('reject').click()

    def go_to_car_review(self):
        self._go_to_task_page()
        return self.find_elements_by_css('.panel-body ul li a')[0].click()

    def click_pass_btn(self):
        self.go_to_car_review()
        self._click_pass_btn()
        time.sleep(3)
        self.find_elements_by_css('.modal-footer .btn')[1].click()
        time.sleep(2)

    def click_fail_btn(self):
        self.go_to_car_review()
        self._click_fail_btn()
        time.sleep(3)
        self.find_element_by_id('reason').send_keys('sorry')
        time.sleep(3)
        self.find_elements_by_css('.modal-footer .btn')[0].click()
        time.sleep(2)







