# -*- coding:utf-8 -*-
from api.base_api.base_api import BaseApi


class MobileIsExistApi(BaseApi):
    """
    验证用户是否存在
    """
    url = '/mobile-is-exist'

    def build_custom_param(self, data):
        return {
            "mobile": data['mobile'],
        }

