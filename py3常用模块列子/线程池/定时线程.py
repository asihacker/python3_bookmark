#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:05
# @Author  : AsiHacker
# @Site    : 
# @File    : 定时线程.py
# @Software: PyCharm
import threading


def test():
    print(123)


if __name__ == '__main__':
    threading.Timer(3, test).start()
    print('456')
