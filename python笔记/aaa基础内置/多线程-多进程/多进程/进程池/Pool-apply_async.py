#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 12:51
# @Author  : AsiHacker
# @File    : Pool-apply_async.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import multiprocessing
import os
import time


# apply_async 方法用来同步执行进程，允许多个进程同时进入池子。
def run_task(name):
    """

    :param name:
    :return:
    """
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))


if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')
