#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 13:45
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime
import sched
import time
from typing import Union


def do_work(a: Union[str, int, float]) -> str:
    """

    :param a:
    :return:
    """
    print(f'{a}')
    return f'{a}'


# sch = sched.scheduler()
# sch.enter()的第一个参数为延迟的时间，单位为秒，第二个参数为优先级，数字越小优先级越高。
# 为什么这里优先级失效了？1的优先级大于2，应该先运行下面的才对啊。
# 这是由于，只有当两个任务同时运行的时候，才会去检查优先级。如果两个任务触发的时间一前一后，那么还轮不到比较优先级。
# 由于延迟队列的延迟是相对于当前运行这一行代码的时间来计算的，后一行代码比前一行代码晚了几毫秒，所以实际上产品经理这一行会先到时间，所以就会先运行。
# sch.enter(3, 2, do_work, argument=('asihacker',))
# sch.enter(3, 1, do_work, kwargs={'a': 123})
# sch.run()


sch = sched.scheduler(time.time, time.sleep)
start_time = datetime.datetime.now() + datetime.timedelta(seconds=3)
start_time_ts = start_time.timestamp()
sch.enterabs(start_time_ts, 2, do_work, argument=('asihacker',))
sch.enterabs(start_time_ts, 1, do_work, kwargs={'a': 123})
sch.run()
