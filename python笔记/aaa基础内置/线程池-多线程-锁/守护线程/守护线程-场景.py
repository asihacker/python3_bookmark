#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 13:13
# @Author  : AsiHacker
# @File    : 守护线程-场景.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

import time
import threading


# 这份代码可能会一直循环打印,现在请看 守护线程-解决办法.py 实现在主线程退出后停止打印，也就是使用守护线程的方法
def test():
    while True:
        print(threading.currentThread())
        time.sleep(0.01)


if __name__ == '__main__':
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test)
    t1.start()
    t2.start()
