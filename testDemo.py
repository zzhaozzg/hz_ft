# -*- coding:utf-8 -*-
import time

import datetime
import urllib

import xlrd
from dateutil.relativedelta import relativedelta
from selenium import webdriver



# token = 'b1989904-a42c-40f3-9ae6-0882657af798'
# print len(token)
# now = datetime.date.today()
# a = str(now)
# print a

# a = datetime.date(year=2016,month=02,day=01)
# b= (a+datetime.timedelta(days=30)).strftime("%Y-%m-%d")
#
# print type(a), b
#
#
# list = [{u'1':u'j'},{u'2':u'k'}]
# a = [1, 2]
# print list[0], a[1]

#
# hei = xlrd.open_workbook('hello.xlsx')
# sheet = hei.sheets()[0]
# # sheet.encode('utf-8')
# for i in range(0, 30):
#     hei =sheet.row_values(i)
#     for i in range(0, 10):
#         a = hei[i]
#         print a
#         # print str(a).decode('unicode-escape').encode('utf-8')

#
# repay_date = datetime.datetime.now()
# repay_date = repay_date +relativedelta(month=1)
# print repay_date


# periods = {'1': 13, '2': 25, '3':37}
# print periods[str(1)]
# date = datetime.datetime.now()
# actual_date = date + datetime.timedelta(days=-1)
# print actual_date, date

# repay_date = '2016-01-01 19:23:04.000001'
#
# first_repay_date=datetime.datetime.strptime(repay_date, "%Y-%m-%d %H:%M:%S.%f")
#
# actual_date = first_repay_date + datetime.timedelta(days=-1)
# repay_date = first_repay_date.strftime("%Y-%m-%d")
# print type(first_repay_date)
# print first_repay_date
# print actual_date
# print repay_date
# repay_date_detail = first_repay_date + relativedelta(months=1)
# repay_date = repay_date_detail.strftime("%Y-%m-%d")
# actual_date = repay_date_detail+datetime.timedelta(days=-1)
# print '====================================================='
# print repay_date_detail
# print actual_date
# print repay_date



# data = {
#             "mobile": 'mobile',
#             "password": 'password',
#             "captcha_hash": 'self.hash_key',
#             "captcha_code": 'captcha_code'
#         }
# login_data = urllib.urlencode(data)
# print  login_data


class Fu(object):

    def haha(self):
        print "haha"

