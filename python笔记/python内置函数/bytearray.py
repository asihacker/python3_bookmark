#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 22:10
# @Author  : AsiHacker
# @Site    : 
# @File    : bytearray.py
# @Software: PyCharm
# 当source参数为字符串时，encoding参数也必须提供，函数将字符串使用str.encode方法转换成字节数组
b = bytearray('fuck你'.encode('utf-8'))
print(len(b))
print(b)
b = bytearray('fuck你', encoding='utf-8')
print(len(b))
print(b.hex())
# 当source参数为整数时，返回这个整数所指定长度的空字节数组
b = bytearray(2)
print(b)
b = u'fuck你'
print(bytes('fuck你'.encode('utf-8')).hex())
