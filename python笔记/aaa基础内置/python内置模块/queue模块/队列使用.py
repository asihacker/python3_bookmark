#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 11:04
# @Author  : AsiHacker
# @Site    : 
# @File    : 队列使用.py
# @Software: PyCharm
from queue import Queue

q = Queue(2)
print(q.put(1))
# print(q.put('bet'))
# # print(q.put('b', block=False))  # block是否阻塞
# print(q.maxsize)  # 队列最大
# print(q.qsize())  # 队列大小
# print(q.full())  # 队列是否满啦
# print(q.empty())  # 队列是否是空
print(q.get())  # 队列取数据
print(q.get())  # 队列取数据
print(q.get(block=False))  # 这里取不到是否阻塞0。0是个坑，要注意。
print(q.get())
