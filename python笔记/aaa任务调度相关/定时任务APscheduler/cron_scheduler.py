#!/usr/bin/python
# coding=utf-8
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


# 指定具体值，或者每分钟，或者每几分钟，或者每周几等当时
#     year (int|str) – 4-digit year
#     month (int|str) – month (1-12)
#     day (int|str) – day of the (1-31)
#     week (int|str) – ISO week (1-53)
#     day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
#     hour (int|str) – hour (0-23)
#     minute (int|str) – minute (0-59)
#     second (int|str) – second (0-59)
#     start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
#     end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
#     timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)


def job_function():
    print("Hello World")


sched = BlockingScheduler()

# 任务会在6月、7月、8月、11月和12月的第三个周五，00:00、01:00、02:00和03:00触发
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')  # second

# start_date 和 end_date 可以用来适用时间范围
# 在2014-05-30 00:00:00前，每周一到每周五 5:30运行
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')


@sched.scheduled_job('cron', id='LogoutNotice', hour='9,11,15')
def LogoutNotice():
    print(" 9点 11点 15点执行")


# 通过 scheduled_job() 装饰器实现：
@sched.scheduled_job('cron', id='my_job_id', day='last sun')
def some_decorated_task():
    print("I am printed at 00:00:00 on the last Sunday of every month!")


# 使用标准crontab表达式：
sched.add_job(job_function, CronTrigger.from_crontab('0 0 1-15 may-aug *'))

# 每小时上下浮动120秒触发
sched.add_job(job_function, 'cron', hour='*', jitter=120)  # 这里也支持震动参数


@sched.scheduled_job('cron', id='debug', second=5)
def test():
    print(datetime.now())
    # 2021-01-05 18:27:05.002295
    # 2021-01-05 18:28:05.006537


sched.start()
