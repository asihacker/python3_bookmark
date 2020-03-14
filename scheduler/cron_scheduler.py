#!/usr/bin/python
# coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def job_function():
    print("Hello World")


sched = BlockingScheduler()

# 任务会在6月、7月、8月、11月和12月的第三个周五，00:00、01:00、02:00和03:00触发
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

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

sched.start()
