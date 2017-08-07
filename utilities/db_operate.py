# -*- coding:utf-8 -*-
from utilities import db

# 获取短信验证码
def get_sms_captcha(mobile):
    db.execute("select substring((select content from sms_log where mobile = %s), 17,4)", params=(mobile))
# 获取图片验证码
def get_captcha(hashkey):
    captcha = db.execute("select response from captcha_captchastore where hashkey = %s", params=(hashkey))
    return captcha['response']
# 删除注册新用户
def clean_user(mobile):

    db.execute("delete from auth_user where username = %s", params=(mobile))
    db.execute("delete from applicant_info where mobile = %s", params=(mobile))
    db.execute("delete from sms_log where mobile = %s", params=(mobile))


def clean_car(brand):
    db.execute("delete from car where brand = %s", params=(brand))


def clean_contract(mobile):
    contract_id = (db.execute("select id from contract where mobile = %s",params=(mobile)))
    if contract_id is not None:
        db.execute("delete from repay_plan where contract_id = (select id from contract where mobile = %s)",
                   params=(mobile))
        db.execute("delete from insurance where contract_id = (select id from contract where mobile = %s)",
                   params=(mobile))
        db.execute("delete from trade_complete where contract_id = (select id from contract where mobile = %s)",
                   params=(mobile))
        db.execute("delete from pay_log where contract_id = (select id from contract where mobile = %s)",
                   params=(mobile))
        db.execute("delete from contract where mobile = %s", params=(mobile))
        db.execute("delete from car where contract_id = %s",
                   params=(contract_id['id']))
        db.execute("delete from trade where contract_id = %s",
                   params=(contract_id['id']))

        db.execute("delete from other_contacts where user_id = (select id from user_profile where mobile = %s)",
                   params=(mobile))
        db.execute("delete from user_profile where mobile = %s", params=(mobile))
        db.execute("delete from car_estimate where user_mobile = %s", params=(mobile))
