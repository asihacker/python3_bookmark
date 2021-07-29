#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:53
# @Author  : AsiHacker
# @File    : Semaphore-getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# coding: utf-8
import threading
import time


# 如果内部计数器的值大于零，将之减一，并返回；如果等于零，则阻塞，并等待其他线程调用 release() 方法以使计数器为正

def fun(semaphore, num):
    # 获得信号量，信号量减一
    semaphore.acquire()
    print("Thread %d is running." % num)
    time.sleep(3)
    # 释放信号量，信号量加一
    semaphore.release()


if __name__ == '__main__':
    # 初始化信号量，数量为2
    semaphore = threading.Semaphore(2)

    # 运行4个线程
    for num in range(4):
        t = threading.Thread(target=fun, args=(semaphore, num))
        t.start()
