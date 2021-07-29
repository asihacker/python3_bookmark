#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 20:09
# @Author  : AsiHacker
# @File    : timeout-decorator模块实现超时机制.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
import traceback

import stopit


# https://www.cnblogs.com/haoxr/p/8757985.html 函数超时机制的几种实现方法

@stopit.threading_timeoutable()
def infinite_loop():
    # As its name says...
    try:
        print("Start")
        for i in range(1, 10):
            print("%d seconds have passed" % i)
            time.sleep(1)
    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == '__main__':
    infinite_loop(timeout=1)
