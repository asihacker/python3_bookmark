#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 22:45
# @Author  : AsiHacker
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import uuid

print(uuid.uuid1().int)
print(uuid.uuid1().hex)
print(uuid.uuid1().time)
print(uuid.uuid1().bytes)
print(uuid.uuid1().clock_seq)
print(uuid.uuid1().clock_seq_low)
print(uuid.uuid1().fields)
