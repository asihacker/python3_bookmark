#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 20:16
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
import re

# https://blog.csdn.net/weixin_38819889/article/details/93846579
c = re.compile('abc')
a = re.search(c, 'www.abc.com')
b = re.match('abc', 'www.abc.com', flags=0)  # flags标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
print(a)
# print(a.groups(),b.group())
help(re)
