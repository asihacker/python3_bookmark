#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 19:40
# @Author  : AsiHacker
# @File    : 进程锁.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import multiprocessing
import time

# lock = multiprocessing.RLock()
lock = multiprocessing.Lock()


def job(v, num, lock):
    lock.acquire()
    for _ in range(50):
        time.sleep(0.1)  # 暂停0.1秒，让输出效果更明显
        v.value += num  # v.value获取共享变量值
        print(v.value, end=",")
    lock.release()


def multicore():
    v = multiprocessing.Value('i', 0)  # 定义共享变量
    p1 = multiprocessing.Process(target=job, args=(v, 1, lock))
    p2 = multiprocessing.Process(target=job, args=(v, 3, lock))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
