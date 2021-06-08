#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 23:28
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
import time
import asyncio


def washing1():
    time.sleep(1)
    print('washing1')


def washing2():
    time.sleep(2)
    print('washing2')


async def washing3():
    time.sleep(3)
    print('washing3')


if __name__ == '__main__':
    print(asyncio.iscoroutinefunction(washing3))
    # 判断是不是 async 修饰的函数
