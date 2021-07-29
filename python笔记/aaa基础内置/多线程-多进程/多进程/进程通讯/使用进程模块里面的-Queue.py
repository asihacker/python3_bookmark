#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:19
# @Author  : AsiHacker
# @File    : 使用进程模块里面的-Queue.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
from multiprocessing import Process
from multiprocessing import Queue


# Queue.Queue是进程内非阻塞队列，multiprocess.Queue是跨进程通信队列。

def producer(food, q, name):
    for i in range(3):
        res = '%s%s' % (food, i)
        time.sleep(1)
        q.put(res)
        print('%s 生产了%s' % (name, res))
    q.put(name)


def consumer(q, name):
    while True:
        res = q.get()
        if res in ("worker_01", "worker_02", "worker_03"):
            print(res, "-------???-------")
            break  # 这里就是区别和joinableQueue 屏蔽掉q.get()会阻塞
        time.sleep(1)
        print('----------%s消费了%s' % (name, res))


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=('包子', q, 'worker_01'))
    p2 = Process(target=producer, args=('水饺', q, 'worker_02'))
    p3 = Process(target=producer, args=('馒头', q, 'worker_03'))

    c1 = Process(target=consumer, args=(q, 'Consumer_01'))
    c2 = Process(target=consumer, args=(q, 'Consumer_02'))

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    print('主...')
