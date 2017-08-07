# -*- coding:utf-8 -*-
ENV = 'test'
# ENV = 'dev'
GECKODRIVER_PATH = '/opt/geckodriver'
CONSOLE_TEST_BASE_URL = 'http://localhost:8000/console'
WAIT_TIME = 10

DB_CONFIG = {
    "HOST": 'localhost',
    "PORT": 3306,
    "USER": 'root',
    "PASSWORD": 'root'
}

REDIS_CONFIG = {
    'HOST': '127.0.0.1',
    'PORT': 6379,
    'SESSION_DB': 3
}


CAR_INFO = {
    'brand' : 'Lamborghini',
    'model' : 'Veneno',
    'displacement' : u'6.5升',
    'vin' : 'JDUEWI8372HSE',
    'engine_number' : '394834348',
    'registration_no': '324972878',
    'year': '2017',
    'plate_number': u'京A88888',
    'price' : '8000000',
    'init_distance' : '0',
    'type' : u'跑车',
    'purpose' : 'cool'

}

CONTRACT_INFO = {
    'area_manager': u'张三',
    'seller': u'李四',
    'risk_manager': u'王五'
}

CLIENT_INFO = {
    'real_name': u'可乐',
    'birthday': '2013-05-04',
    'mobile' : '17300000000',
    'identity_number': '141129197401216956',
    'identity_expire' : '2018-07-21',
    'census_address' : u'北京',
    'live_address': u'北京昌平',
    # 'live_start_date':,
    # 'live_telephone':,
    # 'monthly_income':,
    # 'unit_name':,
    # 'unit_department':,
    # 'unit_address':,
    # 'unit_telephone':,
    # 'unit_position':,
    # 'salary':,
    # 'other_income':,
    # 'unit_join_date':,
    # 'unit_type':,
    # 'founding_date':

}


BRAND = "Lamborghini"
WAIT_FOR_REVIEW = u"待审核"
WAIT_FOR_RENT = u"待租"
REJECT = u"已拒绝"

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
if os.path.exists(SETTING_LOCAL_DIR):
    execfile(SETTING_LOCAL_DIR)

