#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 14:53
# @Author  : AsiHacker
# @Site    : 
# @File    : mongo_scheduler.py
# @Software: PyCharm
import threading
import time

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

jobstores = {
    'mongo': MongoDBJobStore(database='apscheduler', collection='jobs', host='8.129.216.60', port=27017),
}
executors = {
    'default': ThreadPoolExecutor(max_workers=5)
}


def task_func(a):
    print(threading.current_thread().getName())
    print(a)
    return a


# 配置一个调度器对象
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors)
# 给调度器添加定时任务task_func， 指定每日的3点运行一次
scheduler.add_job(task_func, "interval", seconds=3, args=['HelloWord'])
# 开启定时任务


scheduler.start()
while 1:
    pass
