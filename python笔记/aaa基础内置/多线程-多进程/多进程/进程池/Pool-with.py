#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:28
# @Author  : AsiHacker
# @File    : Pool-with.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
import time
from multiprocessing import Pool


def f(x):
    print('Task {0} pid {1} is running, parent id is {2}'.format(x, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(x))
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
