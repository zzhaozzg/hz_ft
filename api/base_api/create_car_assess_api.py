# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class CreateCarAssessApi(LoginBaseApi):
    """
    车辆估值
    """
    url = '/create-car-estimate'

    def build_custom_param(self, data):
        return {
                "car_general": data['car_general'],
                "car_brand": data['car_brand'],
                "mileage": data['mileage'],
                "city": data['city'],
                "user_mobile": data['user_mobile'],
                "car_series": data['car_series'],
                "car_type": data['car_type'],
                "car_bad": data['car_bad'],
                "registration_time": data['registration_time'],
                "car_good": data['car_good']
        }
