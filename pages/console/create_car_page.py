# -*- coding:utf-8 -*-
import time
from selenium.webdriver.support.select import Select

from pages.base_page import BaseConsolePage
from settings import CAR_INFO


class CreateCarPage(BaseConsolePage):

    url = '/car/create-car'

    # def brand(self, brand):
    #     self.find_element_by_id("brand").send_keys(brand)
    #     return self
    #
    # def model(self, model):
    #     self.find_element_by_id("model").send_keys(model)
    #     return self
    #
    # def displacement(self, dis):
    #     self.find_element_by_id("displacement").send_keys(dis)
    #     return self
    #
    # def gearbox(self, gearbox):
    #     return Select(self.find_element_by_id(gearbox)).select_by_index(2)
    #
    # def vin(self, vin):
    #     self.find_element_by_id("vin").send_keys(vin)
    #     return self
    #
    # def engine_number(self, eng):
    #     self.find_element_by_id("engine_number").send_keys(eng)
    #     return self
    #
    # def registration_no(self, no):
    #     self.find_element_by_id("registration_no").send_keys(no)
    #     return self
    #
    # def registration_year(self, year):
    #     pass
    #
    # def plate_number(self, num):
    #     self.find_element_by_id("plate_number").send_keys(num)
    #     return self
    #
    # def price(self, price):
    #     self.find_element_by_id("price").send_keys(price)
    #     return self
    #
    # def init_distance(self, init):
    #     self.find_element_by_id("init_distance").send_keys(init)
    #     return self
    #
    # def accident(self, accident):
    #     pass
    #
    # def type(self, ty):
    #     self.find_element_by_id("type").send_keys(ty)
    #     return self
    #
    # def purpose(self, purpose):
    #     self.find_element_by_id("purpose").send_keys(purpose)
    #     return self
    def _go_to_create_car_page(self):
        self.find_element_by_link_text('新增车辆').click()
        time.sleep(5)

    def create_car(self, brand=CAR_INFO['brand'], model=CAR_INFO['model'], dis=CAR_INFO['displacement'],
                   vin=CAR_INFO['vin'], eng=CAR_INFO['engine_number'], no=CAR_INFO['registration_no'],
                   year=CAR_INFO['year'], num=CAR_INFO['plate_number'], price=CAR_INFO['price'],
                   init=CAR_INFO['init_distance'], ty=CAR_INFO['type'], purpose=CAR_INFO['purpose']):
        self._go_to_create_car_page()

        self.find_element_by_id("brand").send_keys(brand)
        self.find_element_by_id("model").send_keys(model)
        self.find_element_by_id("displacement").send_keys(dis)
        Select(self.find_element_by_id("gearbox")).select_by_index(2)
        self.find_element_by_id("vin").send_keys(vin)
        self.find_element_by_id("engine_number").send_keys(eng)
        self.find_element_by_id("registration_no").send_keys(no)

        js = "$('input[id=registration_year]').removeAttr('readonly')"
        self.execute_js(js)
        self.find_element_by_id('registration_year').send_keys(year)

        self.find_element_by_id("plate_number").send_keys(num)
        self.find_element_by_id("price").send_keys(price)
        self.find_element_by_id("init_distance").send_keys(init)
        Select(self.find_element_by_id("accident")).select_by_index(2)
        self.find_element_by_id("type").send_keys(ty)
        self.find_element_by_id("purpose").send_keys(purpose)
        self.find_element_by_css(".btn.btn-default.pull-right.apply").click()
        self.find_element_by_css(".btn.btn-primary.confirm").click()
        time.sleep(3)