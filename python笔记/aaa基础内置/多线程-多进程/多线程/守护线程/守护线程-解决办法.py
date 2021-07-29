#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 18:21
# @Author  : AsiHacker
# @File    : 守护线程-解决办法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
import threading


def test():
    while True:
        print(threading.currentThread())
        time.sleep(1)


if __name__ == '__main__':
    # 守护进程要设置在start之前
    t1 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()

    t2 = threading.Thread(target=test)
    t2.setDaemon(True)
    t2.start()
