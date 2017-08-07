# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class MyCarApi(LoginBaseApi):
    """
    我的车辆
    """
    url = '/my-car'