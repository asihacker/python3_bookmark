#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 15:30
# @Author  : AsiHacker
# @File    : finditer.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import re

content = '''email:12345678@163.com
email:2345678@163.com
email:345678@163.com
'''
result_finditer = re.finditer(r"\d+@\w+.com", content)
# 由于返回的为MatchObject的iterator，所以我们需要迭代并通过MatchObject的方法输出
for i in result_finditer:
    print(i.group())

result_findall = re.findall(r"\d+@\w+.com", content)
# 返回一个[]  直接输出or或者循环输出
print(result_findall)
for i in result_findall:
    print(i)
