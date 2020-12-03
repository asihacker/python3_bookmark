#!/usr/bin/python
# coding=utf-8
from datetime import datetime, date
# datetime里面有datetime和date两个库
# datetime 用于年月天时分秒
# date用于年月天
from apscheduler.schedulers.blocking import BlockingScheduler

# BlockingScheduler 阻塞式调度器：适用于只跑调度器的程序。
# BackgroundScheduler 后台调度器：适用于非阻塞的情况，调度器会在后台独立运行。
# AsyncIOScheduler AsyncIO调度器，适用于应用使用AsnycIO的情况。
# GeventScheduler Gevent调度器，适用于应用通过Gevent的情况。
# TornadoScheduler Tornado调度器，适用于构建Tornado应用。
# TwistedScheduler Twisted调度器，适用于构建Twisted应用。
# QtScheduler Qt调度器，适用于构建Qt应用。

# date 日期：触发任务运行的具体日期
# interval 间隔：触发任务运行的时间间隔
# cron 周期：触发任务运行的周期
# date: 特定的时间点触发
# interval: 固定时间间隔触发
# cron: 在特定时间周期性地触发

sched = BlockingScheduler()


def my_job(text):
    print(text, 'xiaochen')


# 在2019年9月20日18点27分10秒执行
sched.add_job(my_job, 'date', run_date=datetime(2020, 9, 25, 16, 30, 0), args=['text'])

# sched.add_job(my_job, 'date', run_date=date(2019, 9, 20), args=['text'])

sched.start()  # 调度器是一个循环事件
