#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 13:11
# @Author  : AsiHacker
# @File    : 线程join的理解.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import threading
import time


def test1():
    time.sleep(1)
    print(1)


def test2():
    time.sleep(40)
    print(2)


if __name__ == '__main__':
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    # 如果在这里增加 join 则会线等待执行完t1 与 t2 才会执行 主线程的print(3)
    t1.join(timeout=3)
    t2.join(timeout=3)
    # 如果屏蔽 join 则会线执行print(3)再执行 t1 t2
    print(3)
