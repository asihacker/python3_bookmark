#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 09:16
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
# -*- coding: utf-8 -*-


import os

n = 7
pid = os.fork()  # fork反复拷贝 创建一个子进程
# 如何区别父进程和子进程
# 父进程调用 os.fork = pid
# 子进程调用os.fork = 0

if pid == 0:
    print("A", pid, os.getpid(), os.getppid())
    n -= 1
    print(n)
else:
    print("B", pid, os.getpid(), os.getppid())
    print(n)
