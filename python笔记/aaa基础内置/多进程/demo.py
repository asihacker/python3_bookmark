#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 19:07
# @Author  : AsiHacker
# @File    : task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import multiprocessing


# https://www.cnblogs.com/g2thend/p/12526485.html
import time


def worker(num):
    """thread worker function"""
    time.sleep(10)
    print(multiprocessing.current_process().name)
    print('Worker:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
