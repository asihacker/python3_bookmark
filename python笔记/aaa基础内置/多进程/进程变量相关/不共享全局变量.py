#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:15
# @Author  : AsiHacker
# @File    : 不共享全局变量.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

from multiprocessing import Process
import time

# 进程间是物理隔离的，不共享全局变量
# 子进程是父进程的复制品，在内存中会把父进程的代码及内存分配情况拷贝一份生成子进程的运行空间，
# 这样子进程与父进程的所有代码都一样，两个进程之间的运行时独立的，互不影响
x = 100


def task():
    global x
    x += 1
    print('子进程中执行x所得的值为------%s' % x)
    time.sleep(1)


if __name__ == '__main__':
    p1 = Process(target=task)
    p1.start()
    p1.join()
    print('父进程中执行x所得的值为------%s' % x)
