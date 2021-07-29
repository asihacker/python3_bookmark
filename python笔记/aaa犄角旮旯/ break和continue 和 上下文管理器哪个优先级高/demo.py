# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 14:40
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import contextlib
import time


@contextlib.contextmanager
def runtime(value):
    time.sleep(1)
    print("start: a = " + str(value))
    yield
    print("end: a = " + str(value))


a = 0
while True:
    a += 1
    with runtime(a):
        if a % 2 == 0:
            break

# continue 与 break 一样，如果先遇到上下文管理器会先进行资源的释放
#
# 上面只举例了 while 循环体，而 for 循环也是同样的。
