#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 19:07
# @Author  : AsiHacker
# @File    : task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import multiprocessing
import os


def run_proc(name):
    """
    奔跑进程
    :param name:
    :return:
    """
    print('Child process {0} {1} Running '.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    multiprocessing.Process(target=run_proc, args=('asi',), daemon=True).start()
    multiprocessing.Process(target=run_proc, kwargs={'name': 'asi'}, daemon=True).start()
    multiprocessing.Process(target=run_proc, args=('asi',)).start()
    multiprocessing.Process(target=run_proc, kwargs={'name': 'asi'}).start()
