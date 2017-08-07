# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class WXGenerateOrderApi(LoginBaseApi):
    """
    微信生成订单
    """
    url = '/pay/wx/generate-order'

    def build_custom_param(self, data):
        return {
            "bid": data['bid'],
            "fee_type": data['fee_type']
        }