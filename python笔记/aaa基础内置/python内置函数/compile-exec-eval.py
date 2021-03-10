#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 22:29
# @Author  : AsiHacker
# @Site    : 
# @File    : compile-exec-eval.py
# @Software: PyCharm
# https://www.cnblogs.com/yangmingxianshen/p/7810496.html
str = 'print("hello")'
c = compile(str, '<string>', 'eval')
eval(c)

str = 'print("hello")'
c = compile(str, '<string>', 'eval')
eval(str)

exec(c)  # 直接用这个就好了
str2 = """
bet=1
b=2
print(bet+b)
"""
exec(str2)
str2 = 'bet=1;b=2;print(bet+b)'
exec(str2)
