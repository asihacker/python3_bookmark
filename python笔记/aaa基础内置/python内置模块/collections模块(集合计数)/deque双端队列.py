#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 09:37
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
from collections import deque

# 线程安全
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.appendleft('y')
q.appendleft('y')
print(q.count('y'))
print(q)
