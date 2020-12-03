#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 12:45
# @Author  : AsiHacker
# @File    : testa.py
# @Software: PyCharm
import threading

from python笔记.py3常用模块列子.线程池.线程锁与共享变量.testb import dddd

data = threading.local()


def aaaa(m):
    print(threading.currentThread().getName(), '设置data', m)
    data = m
    dddd()
    return


if __name__ == '__main__':
    for k in range(10):
        threading.Thread(target=aaaa, args=[k]).start()
