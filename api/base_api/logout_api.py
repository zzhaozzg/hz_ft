# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class LogoutApi(LoginBaseApi):
    """
    用户退出登录
    """
    url = '/logout'