#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 23:28
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import time
import asyncio

def washing1():
    time.sleep(1)
    print('washing1')


def washing2():
    time.sleep(2)
    print('washing2')


def washing3():
    time.sleep(3)
    print('washing3')


# if __name__ == '__main__':
#     washing1()
#     washing2()
#     washing3()

if __name__ == '__main__':
    print(asyncio.iscoroutinefunction(washing3))