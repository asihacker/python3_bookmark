#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 22:00
# @Author  : AsiHacker
# @File    : task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
from datetime import datetime

from huey import crontab

from config import huey  # import the huey we instantiated in config.py


# 用task()装饰器简单装饰你想要让消费者运行的函数任务。而当它被调用时候，主进程将立即返回而不是进入函数内部。在消费者进程中会看到这个新消息并运行这个函数。
@huey.task()
def add_numbers(a, b):
    print(a, b)
    print(a + b)
    return a + b


@huey.task(retries=3, retry_delay=10)  # retries 重试次任务 retry_delay 重试延迟时间
def try_thrice():
    print('trying....')
    raise Exception('nope')


@huey.periodic_task(crontab(minute='*'))  # 定时任务
def print_time():
    print(datetime.now())
