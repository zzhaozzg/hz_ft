# -*- coding:utf-8 -*-
import datetime, db
import time
from dateutil.relativedelta import relativedelta

from utilities.fake_user import USER_MOBILE




class InitUser(object):

    def __init__(self):
        self.password = 'pbkdf2_sha256$30000$TnSXtRayVEVR$LoZ2YAqLkohCM7wqezB7LIUTsQ8tNrQTPzqaX0VTv/c='
        self.is_superuser = 0
        self.is_active = 1
        self.first_name = " "
        self.last_name = " "
        self.email = ""
        self.is_staff = 1
        self.date_joined = datetime.datetime.now()

    def _get_contract_id(self):
        contract_id = db.execute("select id from contract where mobile = %s", params=(USER_MOBILE))
        return contract_id['id']

    def _get_car_id(self):
        car_id = db.execute("select id from car where contract_id = (select id from contract where mobile = %s)",
                    params=(USER_MOBILE))
        return  car_id['id']

    def _get_renter_id(self):
        renter_id = db.execute("select id from user_profile where mobile = %s", params=(USER_MOBILE))
        return renter_id['id']

    def _get_trade_id(self):
        trade_id = db.execute("select id from trade where contract_id = "
                    "(select id from contract where mobile = %s)", params=(USER_MOBILE))
        return trade_id['id']

    def create_new_user(self):
        db.execute("insert into auth_user("
                  "password,"
                  "is_superuser,"
                  "username,"
                  "is_active,"
                  "first_name,"
                  "last_name,"
                  "email,"
                  "is_staff,"
                  "date_joined"
                  ")value(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                  params=(self.password, self.is_superuser, USER_MOBILE, self.is_active, self.first_name,
                          self.last_name, self.email, self.is_staff, self.date_joined))
        return self

    def create_car(self, contract_id=None, status='RENTING'):
        db.execute("insert into car("
                   "contract_id,"
                   "brand, "
                   "model, "
                   "displacement, "
                   "gearbox, "
                   "vin, "
                   "engine_number, "
                   "registration_no, "
                   "registration_year, "
                   "plate_number, "
                   "price, "
                   "init_distance, "
                   "current_distance, "
                   "accident, "
                   "type, "
                   "purpose, "
                   "status, "
                   "created_time, "
                   "approved_time, "
                   "reason, "
                   "approver_id, "
                   "creator_id, "
                   "update_time,"
                   "gps_number)"
                   "value(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   params=(contract_id, 'Lamborghini', 'Veneno', u'6.5升', 'MT', 'JDUEWI8372HSE',
                           394834348, 324972878, 2017, u'京A88888',
                           8000000, 0, 0, 0, u'跑车',
                           'cool', status, datetime.datetime.now(),
                           datetime.datetime.now(), '', 1, 1, datetime.datetime.now(), 888888))
        return self

    def _create_user_profile(self, contract_id = None):
        db.execute("insert into user_profile("
                   "contract_id, "
                   "real_name, "
                   "identity_number, "
                   "identity_expire, "
                   "gender, "
                   "birthday, "
                   "mobile, "
                   "census_address, "
                   "live_address, "
                   "live_start_date, "
                   "local_arrive_year, "
                   "live_telephone, "
                   "marital_status, "
                   "have_child, "
                   "education, "
                   "monthly_income, "
                   "house, "
                   "house_rent, "
                   "salary, "
                   "other_income, "
                   "unit_name, "
                   "unit_department, "
                   "unit_address, "
                   "unit_telephone, "
                   "unit_position, "
                   "unit_join_date, "
                   "unit_type, "
                   "company_type, "
                   "founding_date, "
                   "is_coborrower, "
                   "created_time, "
                   "creator_id, "
                   "update_time)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                   "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", params=(contract_id,
                                                                                     u'test',
                                                                                     211122199312123515,
                                                                                     '1983-10-26', 'MALE',
                                                                                     '1983-10-26', USER_MOBILE,
                                                                                     u'河北省石家庄市桥西区',
                                                                                     u'河北省石家庄市桥西区',
                                                                                     '2017-07-02',
                                                                                     '',
                                                                                     '',
                                                                                     u'已婚',
                                                                                     1, '',
                                                                                     9800,
                                                                                     u'无按揭购房', 3000,
                                                                                     3000, 5000,
                                                                                     '',
                                                                                     '',
                                                                                     '',
                                                                                     '',
                                                                                     '',
                                                                                     '2017-03-05',
                                                                                     '',
                                                                                     '',
                                                                                     datetime.datetime.now(),
                                                                                     0,
                                                                                     datetime.datetime.now(), 1,
                                                                                     datetime.datetime.now()))
        return self
    def _create_trade(self, contract_id = None, start_time=datetime.datetime.now().strftime("%Y-%m-%d"),
                      end_time=(datetime.datetime.now()+datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
                      second_repay_date=(datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d")):
        db.execute(
            "insert into trade(contract_id,start_date, period, end_date, car_price, guarantee_amount, annual_rate, "
            "month_principal,month_interest,second_repay_date,survey_fee,gps_fee,left_price,created_time,approved_time,approver_id,"
            "creator_id,update_time)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            params=(contract_id, start_time, 1,
                    end_time, 500000, 6000,
                    0.02, 4166.67, 823.33, second_repay_date,
                    300, 400, 300, datetime.datetime.now(),None,None,1,datetime.datetime.now()))
        return self
    def _create_insurance(self, repay_time=datetime.datetime.now().strftime("%Y-%m-%d"),
                          actual_amount=None, actual_income=None, actual_date=None,
                          approved_time=None, status='GENERATE', approver_id=None,contract_id=None):
        db.execute("insert into insurance("
                   "repay_date,"
                   "amount,"
                   "third_payment_fee,"
                   "actual_amount,"
                   "actual_income,"
                   "actual_date,"
                   "created_time,"
                   "update_time,"
                   "approved_time,"
                   "status,"
                   "trade_time,"
                   "trade_no,"
                   "out_trade_no,"
                   "pay_type,"
                   "approver_id,"
                   "contract_id, "
                   "creator_id)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   params=(repay_time, 3000, 0, actual_amount, actual_income,
                           actual_date, datetime.datetime.now(), datetime.datetime.now(),
                           approved_time, status,
                           None, None, None, None,approver_id, contract_id,1))
        return self

    def _create_contract(self, status):
        # create_contract
        db.execute("insert into contract("
                   "province, "
                   "city, "
                   "area_manager, "
                   "seller, "
                   "risk_manager, "
                   "created_time, "
                   "approved_time, "
                   "status, "
                   "real_name, "
                   "identity_number, "
                   "mobile, "
                   "approver_id, "
                   "car_id, "
                   "coborrower_id, "
                   "creator_id, "
                   "merchant_id, "
                   "renter_id, "
                   "trade_id, "
                   "update_time"
                   ")values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   params=(u'河北', u'石家庄', u'蒲立强', u'王丛姗', u'李一伟',
                           datetime.datetime.now(), datetime.datetime.now(), status, u'test', 211122199312123515,
                           USER_MOBILE, 1, None, None, 1,
                           None, 1, None, datetime.datetime.now()))
        return self

    def _create_repay_plan(self, years, overdue_fee=None, third_payment_fee=None,
                           first_repay_date=datetime.datetime.now(),
                           actual_amount=None,actual_income=None,
                           status='GENERATE',approver_id=None, contract_id=None):
        periods = {'1': 13, '2': 25, '3':37}


        actual_date = first_repay_date+datetime.timedelta(days=-1)
        repay_date = first_repay_date.strftime("%Y-%m-%d")

        for period in range(1, periods[str(years)]):
            db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
                       "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,"
                       "status,trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
                       "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       params=(period, 4166.67, 823.33, overdue_fee,third_payment_fee, repay_date, actual_amount,
                               actual_income, actual_date, 0, datetime.datetime.now(),
                               datetime.datetime.now(), datetime.datetime.now(),
                               status, None, None, None, None, approver_id, contract_id, 1))
            repay_date_detail = first_repay_date + relativedelta(months=1)
            repay_date = repay_date_detail.strftime("%Y-%m-%d")

            actual_date = repay_date_detail+datetime.timedelta(days=-1)
        return self


    def _create_trade_complete(self, contract_id):
        db.execute("insert into trade_complete(complete_way,left_price,guarantee_amount,deduct_guarantee,"
                   "left_guarantee,actual_pay,addition,created_time,reject_reason,is_approver,approved_time,"
                   "approver_id,contract_id,creator_id,update_time)"
                   "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   params=(u'退款租赁物', 300, 6000, 0, 6000, 6000, '', datetime.datetime.now(), '', 0,
                           datetime.datetime.now(), 1, contract_id, 1, datetime.datetime.now()))

    def _update_contract(self):
        self.car_id = self._get_car_id()
        self.renter_id = self._get_renter_id()
        self.trade_id = self._get_trade_id()

        db.execute("update contract set car_id = %s, renter_id = %s, trade_id =%s where mobile = %s",
                   params=(self.car_id, self.renter_id, self.trade_id, USER_MOBILE))

    def create_completed_contract(self):
        #create_old_contract
        self._create_contract(status='COMPLETED')
        # db.execute("insert into contract("
        #            "province, "
        #            "city, "
        #            "area_manager, "
        #            "seller, "
        #            "risk_manager, "
        #            "created_time, "
        #            "approved_time, "
        #            "status, "
        #            "real_name, "
        #            "identity_number, "
        #            "mobile, "
        #            "approver_id, "
        #            "car_id, "
        #            "coborrower_id, "
        #            "creator_id, "
        #            "merchant_id, "
        #            "renter_id, "
        #            "trade_id, "
        #            "update_time"
        #            ")values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(u'河北', u'石家庄', u'蒲立强', u'王丛姗', u'李一伟',
        #                    datetime.datetime.now(), datetime.datetime.now(), 'COMPLETED', u'test', 211122199312123515,
        #                    USER_MOBILE, 1, None, None, 1,
        #                    None, 1, None, datetime.datetime.now()))
        self.contract_id = self._get_contract_id()
        # create_car
        self.create_car(contract_id=self.contract_id, status='TO_BE_RENTED')
        # db.execute("insert into car("
        #            "contract_id, "
        #            "brand, "
        #            "model, "
        #            "displacement, "
        #            "gearbox, "
        #            "vin, "
        #            "engine_number, "
        #            "registration_no, "
        #            "registration_year, "
        #            "plate_number, "
        #            "price, "
        #            "init_distance, "
        #            "current_distance, "
        #            "accident, "
        #            "type, "
        #            "purpose, "
        #            "status, "
        #            "created_time, "
        #            "approved_time, "
        #            "reason, "
        #            "approver_id, "
        #            "creator_id, "
        #            "update_time)"
        #            "value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(self.contract_id, 'Lamborghini', 'Veneno', u'6.5升', 'MT', 'JDUEWI8372HSE',
        #                    394834348, 324972878, 2017, u'京A88888',
        #                    8000000, 0, 0, 0, u'跑车',
        #                    'cool', 'TO_BE_RENTED', datetime.datetime.now(),
        #                    datetime.datetime.now(), '', 1, 1, datetime.datetime.now()))
        #create_old_user_profile
        self._create_user_profile(contract_id=self.contract_id)
        # db.execute("insert into user_profile("
        #            "contract_id, "
        #            "real_name, "
        #            "identity_number, "
        #            "identity_expire, "
        #            "gender, "
        #            "birthday, "
        #            "mobile, "
        #            "census_address, "
        #            "live_address, "
        #            "live_start_date, "
        #            "local_arrive_year, "
        #            "live_telephone, "
        #            "marital_status, "
        #            "have_child, "
        #            "education, "
        #            "monthly_income, "
        #            "house, "
        #            "house_rent, "
        #            "salary, "
        #            "other_income, "
        #            "unit_name, "
        #            "unit_department, "
        #            "unit_address, "
        #            "unit_telephone, "
        #            "unit_position, "
        #            "unit_join_date, "
        #            "unit_type, "
        #            "company_type, "
        #            "founding_date, "
        #            "is_coborrower, "
        #            "created_time, "
        #            "creator_id, "
        #            "update_time)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
        #            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", params=(self.contract_id,
        #                                                                       u'test',
        #                                                                       211122199312123515,
        #                                                                       '1983-10-26', 'MALE',
        #                                                                       '1983-10-26', 17300000000,
        #                                                                       u'河北省石家庄市桥西区',
        #                                                                       u'河北省石家庄市桥西区',
        #                                                                       '2017-07-02',
        #                                                                       '',
        #                                                                       '',
        #                                                                       u'已婚',
        #                                                                       1, '',
        #                                                                       9800,
        #                                                                       u'无按揭购房', 3000,
        #                                                                       3000, 5000,
        #                                                                       '',
        #                                                                       '',
        #                                                                       '',
        #                                                                       '',
        #                                                                       '',
        #                                                                       '2017-03-05',
        #                                                                       '',
        #                                                                       '',
        #                                                                       datetime.datetime.now(),
        #                                                                       0,
        #                                                                       datetime.datetime.now(), 1,
        #                                                                       datetime.datetime.now()))
        # create_old_trade
        self._create_trade(contract_id=self.contract_id,
                           start_time='2016-01-01',
                           end_time='2016-12-31',
                           second_repay_date='2016-02-01')
        # db.execute(
        #     "insert into trade(contract_id,start_date, period, end_date, car_price, guarantee_amount, annual_rate, "
        #     "month_principal,month_interest,second_repay_date,survey_fee,gps_fee,left_price,created_time,approved_time,approver_id,"
        #     "creator_id,update_time)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #     params=(self.contract_id, '2016-01-01', 1,
        #             '2016-12-31', 500000, 6000,
        #             0.02, 4166.67, 823.33, '2016-02-01',
        #             300, 400, 300, datetime.datetime.now(),None,None,1,datetime.datetime.now()))

        #create_old_insurance
        self._create_insurance(repay_time='2016-01-07',
                               actual_amount=3000,
                               actual_income=3000,
                               actual_date='2016-01-06 16:00:00.000000',
                               approved_time=datetime.datetime.now(),
                               status='COMPLETE',
                               approver_id=1,
                               contract_id=self.contract_id)
        # db.execute("insert into insurance("
        #            "repay_date,"
        #            "amount,"
        #            "third_payment_fee,"
        #            "actual_amount,"
        #            "actual_income,"
        #            "actual_date,"
        #            "created_time,"
        #            "update_time,"
        #            "approved_time,"
        #            "status,"
        #            "trade_time,"
        #            "trade_no,"
        #            "out_trade_no,"
        #            "pay_type,"
        #            "approver_id,"
        #            "contract_id, "
        #            "creator_id)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=('2016-01-07', 3000, 0, 3000, 3000,
        #                    '2016-01-06 16:00:00.000000', datetime.datetime.now(), datetime.datetime.now(),
        #                    datetime.datetime.now(), 'COMPLETE',
        #                    None, None, None, None, 1, self.contract_id, 1))

        date= '2016-01-01 19:23:04.040000'
        self._create_repay_plan(years=1,
                                overdue_fee=0,
                                third_payment_fee=0,
                                first_repay_date=datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S.%f"),
                                actual_amount=4990,
                                actual_income=4990,
                                status='COMPLETE',
                                approver_id=1,
                                contract_id=self.contract_id)
        #
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(1, 4166.67, 823.33, 0, 0, '2016-01-01', 4990, 4990, '2015-12-31 16:00:00.000000',
        #                    0,  datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        #
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(2, 4166.67, 823.33, 0, 0, '2016-02-01', 4990, 4990, '2016-01-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(3, 4166.67, 823.33, 0, 0, '2016-03-01', 4990, 4990, '2016-02-29 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(4, 4166.67, 823.33, 0, 0, '2016-04-01', 4990, 4990, '2016-03-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(5, 4166.67, 823.33, 0, 0, '2016-05-01', 4990, 4990, '2016-04-30 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(6, 4166.67, 823.33, 0, 0, '2016-06-01', 4990, 4990, '2016-05-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(7, 4166.67, 823.33, 0, 0, '2016-07-01', 4990, 4990, '2016-06-30 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        #
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(8, 4166.67, 823.33, 0, 0, '2016-08-01', 4990, 4990, '2016-07-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(9, 4166.67, 823.33, 0, 0, '2016-09-01', 4990, 4990, '2016-08-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(10, 4166.67, 823.33, 0, 0, '2016-10-01', 4990, 4990, '2016-09-30 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(11, 4166.67, 823.33, 0, 0, '2016-11-01', 4990, 4990, '2016-10-31 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        # db.execute("insert into repay_plan (period,principal,interest,overdue_fee,third_payment_fee,repay_date,"
        #            "actual_amount,actual_income,actual_date,is_continue,created_time,update_time,approved_time,status,"
        #            "trade_time,trade_no,out_trade_no,pay_type,approver_id,contract_id,creator_id)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(12, 4166.67, 823.33, 0, 0, '2016-12-01', 4990, 4990, '2016-11-30 16:00:00.000000',
        #                    0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
        #                    'COMPLETE', None, None, None, None, 1, self.contract_id, 1))
        self._create_trade_complete(contract_id=self.contract_id)
        # db.execute("insert into trade_complete(complete_way,left_price,guarantee_amount,deduct_guarantee,"
        #            "left_guarantee,actual_pay,addition,created_time,reject_reason,is_approver,approved_time,"
        #            "approver_id,contract_id,creator_id,update_time)"
        #            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #            params=(u'退款租赁物', 300, 6000, 0, 6000, 6000, '', datetime.datetime.now(),'',0,
        #                    datetime.datetime.now(), 1, self.contract_id, 1, datetime.datetime.now()))

        # self.car_id = (db.execute("select id from car where contract_id = (select id from contract where mobile = %s)",
        #                     params=(USER_MOBILE)))['id']
        # self.renter_id = (db.execute("select id from user_profile where mobile = %s", params=(USER_MOBILE)))['id']
        # self.trade_id = (db.execute("select id from trade where contract_id = "
        #                            "(select id from contract where mobile = %s)", params=(USER_MOBILE)))['id']

        # self.car_id = self._get_car_id()
        # self.renter_id = self._get_renter_id()
        # self.trade_id = self._get_trade_id()
        #
        # db.execute("update contract set car_id = %s, renter_id = %s, trade_id =%s where mobile = %s",
        #            params=(self.car_id, self.renter_id, self.trade_id, USER_MOBILE))

        self._update_contract()

    def get_repay_id(self):
        return db.execute("select id from repay_plan where contract_id = (select id from contract where mobile = %s)",
                    params=(USER_MOBILE), is_fetchone=False)

    def get_insurance_id(self):
        insurance_id = db.execute("select id from insurance where contract_id = %s", params=(self._get_contract_id()))
        return insurance_id['id']

    def create_contract(self):
        self._create_contract(status='RENTING')
        self.contract_id = self._get_contract_id()
        self.create_car(contract_id=self.contract_id)
        self._create_user_profile(contract_id=self.contract_id)
        self._create_trade(contract_id=self.contract_id)
        self._create_insurance(approver_id=1,
                               contract_id=self.contract_id)
        self._create_repay_plan(years=1,
                                approver_id=1,
                                contract_id=self.contract_id)
        self._update_contract()




