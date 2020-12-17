#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 20:35
# @Author  : AsiHacker
# @Site    : 
# @File    : thread_scheduler.py
# @Software: PyCharm
import threading
import time

from apscheduler.executors.pool import ThreadPoolExecutor

# 执行器配置：使用线程池运行定时任务，且最大线程数为5个
from apscheduler.schedulers.background import BackgroundScheduler

executors = {
    'default': ThreadPoolExecutor(max_workers=500)
}


def task_func(a):
    print(threading.current_thread().getName())
    time.sleep(3)
    print(a)
    return a


# 配置一个调度器对象
scheduler = BackgroundScheduler(executors=executors)
# 给调度器添加定时任务task_func， 指定每日的3点运行一次
scheduler.add_job(task_func, "interval", seconds=1, args=['HelloWord'])
# 开启定时任务


scheduler.start()
while 1:
    pass
