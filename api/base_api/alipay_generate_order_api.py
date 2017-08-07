# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class AlipayGenerateOrderApi(LoginBaseApi):

    """
    支付宝生成订单号
    """
    url = '/pay/alipay/generate-order'

    def build_custom_param(self, data):
        return {
            'bid': data['bid'],
            'fee_type': data['fee_type']
        }