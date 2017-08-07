# -*- coding:utf-8 -*-
import json

import requests

from api import settings
from api.settings import API_TEST_BASE_URL
from utilities.fake_user import USER_MOBILE

class BaseApi(object):
    url = ""

    def __init__(self, mobile=USER_MOBILE,  url_params=None):
        self.mobile = mobile
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = API_TEST_BASE_URL


    def api_url(self):
        if not self.url:
            raise RuntimeError("no url been set")
        return self._get_url()

    def _get_url(self):
        format_url = self.url.format(self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    def post(self, data=None, token=None):
        if not data:
            data = {}
        self.headers()['token'] = token
        custom_param = self.build_custom_param(data)
        data.update(custom_param)
        self.response = requests.post(url=self.api_url(),
                                      json=data,
                                      headers=self.headers(),
                                      )
        return self.response

    def get(self, data=None):
        if not data:
            data = {}
        custom_param = self.build_custom_param(data)
        data.update(custom_param)
        self.response = requests.get(url=self.api_url(),
                                      json=data,
                                      headers=self.headers())
        return self.response

    def get_code(self):
        if self.response:
            return json.loads(self.response.text)['code']

    def get_status_code(self):
        if self.response:
            return self.response.status_code

    def get_response_message(self):
        if self.response:
            return json.loads(self.response.text)['message']

    def build_custom_param(self, data):
        return {}

    def headers(self):
        return {
            'token': '',
            'Content-Type': 'application/json;charset=utf-8',
            'platform': 'ios'
        }