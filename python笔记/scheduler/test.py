#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 13:10
# @Author  : AsiHacker
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import datetime
import time

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler


class Apple(object):
    def __init__(self):
        self.jobstores = {'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')}
        self.sche = BackgroundScheduler(jobstores=self.jobstores)
        self.sche.start()

    def get_time(self, x):
        return datetime.datetime.now() + datetime.timedelta(seconds=x)

    def test(self):
        time = self.get_time(3)
        self.sche.add_job(self.test2, next_run_time=time, args=[1, 2])

    def test2(self, a, b):
        print(a, b)


aa = Apple()
aa.test()
while 1:
    time.sleep(1)
