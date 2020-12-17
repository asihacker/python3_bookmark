#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:23
# @Author  : AsiHacker
# @Site    : 
# @File    : diaoyong.py.py
# @Software: PyCharm
from python笔记.aaa任务调度相关.celery任务调度神器.proj import add
import time

t1 = time.time()

r1 = add.delay(1, 2)
r2 = add.delay(2, 4)
r3 = add.delay(3, 6)
r4 = add.delay(4, 8)
r5 = add.delay(5, 10)

r_list = [r1, r2, r3, r4, r5]
for r in r_list:
    while not r.ready():
        pass
    print(r.result)

t2 = time.time()

print('共耗时：%s' % str(t2 - t1))
