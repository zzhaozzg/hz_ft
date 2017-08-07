# -*- coding:utf-8 -*-
from api.base_api.login_base_api import LoginBaseApi


class RepayPlanDetailApi(LoginBaseApi):
    """
    往期账单明细
    """
    url = '/repay-plan-detail'

    def build_custom_param(self, data):

        return {
            "repayId": data['repayId']
        }