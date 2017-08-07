# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class MyFundApi(LoginBaseApi):
    """
    资金明细
    """
    url = '/my-fund'
