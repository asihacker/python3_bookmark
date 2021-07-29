# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:42
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
import timeit


def run_sleep(second):
    print(second)
    time.sleep(second)


# 只用这一行
print(timeit.timeit(lambda: run_sleep(2), number=5))
