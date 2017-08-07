# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class InsuranceDetailApi(LoginBaseApi):
    """
    保险费用明细
    """
    url = '/insurance-detail'

    def build_custom_param(self, data):
        return {
            "bid": data['bid']
        }