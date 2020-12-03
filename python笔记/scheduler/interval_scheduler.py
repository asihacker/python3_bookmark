#!/usr/bin/python
# coding=utf-8
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import threading, time


def job_function():
    print("Hello World")


sched = BlockingScheduler()

# 每2小时触发
sched.add_job(job_function, 'interval', hours=2)
"""
weeks (int) 间隔几周
days (int) 间隔几天
hours (int) 间隔几小时
minutes (int) 间隔几分钟
seconds (int) 间隔多少秒
"""
# 周期触发的时间范围在2010-10-10 9:30 至 2014-06-15 11:00
sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')


# 也可以通过scheduled_job()装饰器实现
@sched.scheduled_job('interval', id='my_job_id', seconds=2)
def job_function():
    print("Hello World")


# 每小时（上下浮动120秒区间内）运行`job_function`
sched.add_job(job_function, 'interval', hours=1, jitter=120)
# jitter振动参数，给每次触发添加一个随机浮动秒数，一般适用于多服务器，避免同时运行造成服务拥堵。

threading.Thread(target=sched.start).start()
print(123)
while True:
    time.sleep(1)
