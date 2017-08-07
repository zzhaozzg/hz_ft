# -*- coding=utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class ModifyPassWordApi(LoginBaseApi):
    """
    修改密码
    """
    url = "/modify-password"

    def build_custom_param(self, data):
        return{
                "oldPassword": data['oldPassword'],
                "password": data['password']
        }