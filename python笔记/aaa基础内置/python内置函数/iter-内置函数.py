#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 00:35
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
a = ['我', 'ai', 'ni', 'zg']
# b = range(20)#这是一个范围的基础类型 有三种基本的序列类型：列表、元组和范围（range）对象。！！！！！！！！
# b = iter(range(20))  # 这是可迭代对象
b = (k for k in range(20))  # 这是生成器
for k in b:
    print(k, sep='\t', end='   ')
