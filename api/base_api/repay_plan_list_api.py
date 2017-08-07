# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class RepayPlanListApi(LoginBaseApi):
    """
    往期账单列表
    """
    url = '/repay-plan-list'