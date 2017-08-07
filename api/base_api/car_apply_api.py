# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class CarApplyApi(LoginBaseApi):
    """
    申请租车
    """
    url = '/car-apply'

    def build_custom_param(self, data):
        return {
            "car_brand": data['car_brand'],
            "car_price": data['car_price']
        }