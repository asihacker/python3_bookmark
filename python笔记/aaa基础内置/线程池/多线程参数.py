#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 19:10
# @Author  : AsiHacker
# @Site    : 
# @File    : 多线程参数.py
# @Software: PyCharm

import threading
from concurrent.futures import ThreadPoolExecutor

num = 0
lock = threading.Lock()


def test():
    global num
    global lock
    for _ in range(10000000):
        lock.acquire()
        num += 1
        lock.release()
    return


# if __name__ == '__main__':
#     threading.Thread(target=test(1, 2, 3)).start()
if __name__ == '__main__':
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
