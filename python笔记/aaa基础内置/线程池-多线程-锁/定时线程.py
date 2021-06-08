#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:05
# @Author  : AsiHacker
# @Site    : 
# @File    : 定时线程.py
# @Software: PyCharm
import threading


def test():
    print(threading.get_ident())  # 返回线程pid
    print(threading.main_thread())  # 返回主线程对象，类似 threading.current_thread()；只不过一个是返回当前线程对象，一个是返回主线程对象
    print(threading.get_native_id)


if __name__ == '__main__':
    threading.Timer(3, test).start()
    print(threading.enumerate())  # 返回线程列表
    print('456')
