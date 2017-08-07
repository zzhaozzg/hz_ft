from pages.base_page import BaseConsolePage


class CarListPage(BaseConsolePage):

    url = '/car/car-list'

    def get_apply_car_status(self):
        status = self.find_element_by_css('.table tbody tr:nth-of-type(1) td:nth-of-type(6)').text
        return status

    def get_apply_car_model(self):
        model = self.find_element_by_css('.table tbody tr:nth-of-type(1) td:nth-of-type(2)').text
        return model