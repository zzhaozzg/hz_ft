import json

from api.base_api.base_api import BaseApi
from api.base_api.login_api import LoginApi

class LoginBaseApi(BaseApi):

    platform = 'iOS'
    def __init__(self, mobile, password, *args, **kwargs):
        super(LoginBaseApi, self).__init__(*args, **kwargs)
        self.password = password
        self.mobile = mobile

    def headers(self):
        rep = LoginApi().login(self.mobile, self.password)
        rep_token = json.loads(rep.content)['token']
        param = {
            'token': rep_token,
            'Content-Type': 'application/json;charset=utf-8',
            'platform': self.platform
        }
        return param