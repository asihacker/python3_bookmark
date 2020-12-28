#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 22:04
# @Author  : AsiHacker
# @File    : main.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

from past.builtins import raw_input

from task import try_thrice

# https://github.com/coleifer/huey
# huey_consumer.py task.huey -k process -w 4 通过进程启动
# huey_consumer.py task.huey -k thread -w 4 通过线程启动
# huey_consumer.py task.huey -k greenlet -w 4 通过事件启动

# 获取结果
# 1.res.get_raw_result(blocking=True)
# 2.res.get()
# 3.res()

if __name__ == '__main__':
    for beans in range(5):
        time.sleep(1)
        # res = add_numbers(beans,beans)#常规任务
        res = try_thrice()  # 重试次任务
        print('任务id', res.id)
        print('我是任务结果', res.get_raw_result(blocking=True))
