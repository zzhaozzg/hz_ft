# -*- coding:utf-8 -*-
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
from pages.base_page import BaseConsolePage


class CreateContractPage(BaseConsolePage):

    url = '/contract/customer/0'

    def create_contract(self, area_manager='A', seller='A', risk_manager='A',real_name='test', birthday='1983-05-03',
                      mobile='17300000000', identity_number='140822198505278323', identity_expire='2099-09-09',
                      census_address=u'山西', live_address=u'昌平', live_start_date='2016-06-09',
                      live_telephone='', monthly_income='', unit_name='', unit_department='', unit_address='',
                      unit_telephone='', unit_position='', salary='', other_income='', unit_join_date='', unit_type='',
                      founding_date='', start_date=datetime.datetime.now().strftime("%Y-%m-%d"), guarantee_amount=3000,
                      annual_rate_percent=4, second_repay_date=(datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d"), survey_fee='200', gps_fee='500',
                      left_price='5000000', insurance_year_1_date='2017-08-30', insurance_year_1_amount='3000'):
        Select(self.find_element_by_id('province')).select_by_index(2)
        Select(self.find_element_by_id('city')).select_by_index(2)
        self.find_element_by_id('area_manager').send_keys(area_manager)
        self.find_element_by_id('seller').send_keys(seller)
        self.find_element_by_id('risk_manager').send_keys(risk_manager)
        # client_info
        self.find_element_by_id('real_name').send_keys(real_name)
        Select(self.find_element_by_id('gender')).select_by_index(1)
        self.find_element_by_id('birthday').send_keys(birthday)
        self.find_element_by_id('mobile').send_keys(mobile)
        self.find_element_by_id('identity_number').send_keys(identity_number)
        self.find_element_by_id('identity_expire').send_keys(identity_expire)
        self.find_element_by_id('census_address').send_keys(census_address)
        self.find_element_by_id('live_address').send_keys(live_address)
        self.find_element_by_id('live_start_date').send_keys(live_start_date)
        Select(self.find_element_by_id('local_arrive_year')).select_by_index(1)
        self.find_element_by_id('live_telephone').send_keys(live_telephone)
        Select(self.find_element_by_id('marital_status')).select_by_index(1)
        Select(self.find_element_by_id('have_child')).select_by_index(1)
        Select(self.find_element_by_id('education')).select_by_index(4)
        self.find_element_by_id('monthly_income').send_keys(monthly_income)
        Select(self.find_element_by_id('house')).select_by_index(1)
        self.find_element_by_id('unit_name').send_keys(unit_name)
        self.find_element_by_id('unit_department').send_keys(unit_department)
        self.find_element_by_id('unit_address').send_keys(unit_address)
        self.find_element_by_id('unit_telephone').send_keys(unit_telephone)
        self.find_element_by_id('unit_position').send_keys(unit_position)
        self.find_element_by_id('salary').send_keys(salary)
        self.find_element_by_id('other_income').send_keys(other_income)
        self.find_element_by_id('unit_join_date').send_keys(unit_join_date)
        self.find_element_by_id('unit_type').send_keys(unit_type)
        Select(self.find_element_by_id('company_type')).select_by_index(1)
        self.find_element_by_id('founding_date').send_keys(founding_date)
        self.find_elements_by_css('.btn.btn-default')[1].click()
        time.sleep(5)
        # car_info
        self.find_elements_by_css('.btn.btn-default.dropdown-toggle')[0].click()
        time.sleep(2)
        self.find_elements_by_css('.dropdown-menu.valid-cars-list li')[1].click()
        time.sleep(2)
        self.find_elements_by_css('.btn.btn-default')[3].click()
        #car_trade_info
        self.find_element_by_id('start_date').send_keys(start_date)
        Select(self.find_element_by_id('period')).select_by_index(1)
        self.find_element_by_id('guarantee_amount').send_keys(guarantee_amount)
        self.find_element_by_id('annual_rate_percent').send_keys(annual_rate_percent)
        self.find_element_by_id('second_repay_date').send_keys(second_repay_date)
        self.find_element_by_id('survey_fee').send_keys(survey_fee)
        self.find_element_by_id('gps_fee').send_keys(gps_fee)
        self.find_element_by_id('left_price').send_keys(left_price)
        #insurance_payment_info
        self.find_element_by_name('insurance_year_1_date').send_keys(insurance_year_1_date)
        self.find_element_by_name('insurance_year_1_amount').send_keys(insurance_year_1_amount)
        self.find_element_by_name('insurance_year_1_amount').click()
        time.sleep(5)
        self.find_elements_by_css('.btn.btn-default')[1].click()
        time.sleep(5)
        self.find_elements_by_css('.btn.btn-default')[1].click()
        time.sleep(5)
        return self

    def approve_contract(self):
        self.find_element_by_link_text('待办任务').click()
        time.sleep(3)
        self.find_elements_by_css('.panel-body ul li a')[0].click()
        time.sleep(3)
        self.find_elements_by_css('.btn.btn-default')[1].click()
        time.sleep(5)
        self.find_elements_by_css('.btn.btn-primary')[0].click()
        return self




    # def contact_person(self, direct_kinsfolk_name, direct_kinsfolk_relation, direct_kinsfolk_work_unit,
    #                    direct_kinsfolk_address, direct_kinsfolk_phone_number, kinsfolk_name, kinsfolk_relation,
    #                    kinsfolk_work_unit, kinsfolk_address, kinsfolk_phone_number, work_voucher_name,
    #                    work_voucher_relation, work_voucher_work_unit, work_voucher_address, work_voucher_phone_number):
    #
    #     self.find_element_by_id('direct_kinsfolk_name').send_keys(direct_kinsfolk_name)
    #     self.find_element_by_id('direct_kinsfolk_relation').send_keys(direct_kinsfolk_relation)
    #     self.find_element_by_id('direct_kinsfolk_work_unit').send_keys(direct_kinsfolk_work_unit)
    #     self.find_element_by_id('direct_kinsfolk_address').send_keys(direct_kinsfolk_address)
    #     self.find_element_by_id('direct_kinsfolk_phone_number').send_keys(direct_kinsfolk_phone_number)
    #     self.find_element_by_id('kinsfolk_name').send_keys(kinsfolk_name)
    #     self.find_element_by_id('kinsfolk_relation').send_keys(kinsfolk_relation)
    #     self.find_element_by_id('kinsfolk_work_unit').send_keys(kinsfolk_work_unit)
    #     self.find_element_by_id('kinsfolk_address').send_keys(kinsfolk_address)
    #     self.find_element_by_id('kinsfolk_phone_number').send_keys(kinsfolk_phone_number)
    #     self.find_element_by_id('work_voucher_name').send_keys(work_voucher_name)
    #     self.find_element_by_id('work_voucher_relation').send_keys(work_voucher_relation)
    #     self.find_element_by_id('work_voucher_work_unit').send_keys(work_voucher_work_unit)
    #     self.find_element_by_id('work_voucher_address').send_keys(work_voucher_address)
    #     self.find_element_by_id('work_voucher_phone_number').send_keys(work_voucher_phone_number)

    # def car_info(self):
    #     self.find_elements_by_css('.btn.btn-default.dropdown-toggle')[0].click()
    #     self.find_elements_by_css('.dropdown-menu.valid-cars-list li')[1].click()
    #     self.find_elements_by_css('.btn.btn-default')[3].click()
    #
    # def trade_info(self, start_date=datetime.datetime.now(), guarantee_amount=3000, annual_rate_percent=1,
    #                second_repay_date='2017-08-08', survey_fee='200', gps_fee='500',
    #                left_price='5000000'):
    #     self.find_element_by_id('start_date').send_keys(start_date)
    #     Select(self.find_element_by_id('period')).select_by_index(3)
    #     self.find_element_by_id('guarantee_amount').send_keys(guarantee_amount)
    #     self.find_element_by_id('annual_rate_percent').send_keys(annual_rate_percent)
    #     self.find_element_by_id('second_repay_date').send_keys(second_repay_date)
    #     self.find_element_by_id('survey_fee').send_keys(survey_fee)
    #     self.find_element_by_id('gps_fee').send_keys(gps_fee)
    #     self.find_element_by_id('left_price').send_keys(left_price)
    #
    # def insurance_payment_info(self, insurance_year_1_date='2017-08-30', insurance_year_1_amount='3000'):
    #     self.find_element_by_name('insurance_year_1_date').send_keys(insurance_year_1_date)
    #     self.find_element_by_name('insurance_year_1_amount').send_keys(insurance_year_1_amount)
    #
    # def commit_btn(self):
    #     self.find_elements_by_css('.btn.btn-default')[1].click()