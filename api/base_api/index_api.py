# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class IndexApi(LoginBaseApi):
    """
    正常租用用户首页
    """
    url = '/index'