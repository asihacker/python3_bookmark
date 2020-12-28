#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 20:16
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
import re

a = re.search('abc', 'www.abc.com')
b = re.match('abc', 'www.abc.com')
print(a,b)
print(a.groups(),b.group())

