#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:17
# @Author  : AsiHacker
# @File    : 进程join.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
import time
from multiprocessing import Process


def pro_func01(name):
    print("Child process %s (%s)" % (name, os.getpid()))


def pro_func02(name):
    for i in range(5):
        time.sleep(1)
        print("一共睡眠了 %s 秒种" % i)
    print("Child process %s (%s)" % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent process %s" % (os.getpid()))
    p01 = Process(target=pro_func01, args=(str(1),))
    p02 = Process(target=pro_func02, args=(str(2),))
    p01.start()
    p02.start()
    # 这里的join和线程的一样
    p02.join()
    print("Finished")
