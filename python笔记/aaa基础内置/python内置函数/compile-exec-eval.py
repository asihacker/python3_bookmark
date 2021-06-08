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
eval(c)  # 计算指定表达式的值。也就是说它要执行的python代码只能是单个表达式（注意eval不支持任何形式的赋值操作），而不能是复杂的代码逻辑。

str = 'print("hello")'
c = compile(str, '<string>', 'eval')
eval(str)

exec(c)  # 动态执行python代码。也就是说exec可以执行复杂的python代码，而不像eval函数那样只能计算一个表达式的值。
str2 = """
bet=1
b=2
print(bet+b)
"""
exec(str2)
str2 = 'bet=1;b=2;print(bet+b)'
exec(str2)
