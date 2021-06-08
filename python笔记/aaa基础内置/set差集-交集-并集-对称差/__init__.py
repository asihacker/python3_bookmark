#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 10:42
# @Author  : AsiHacker
# @File    : __init__.py.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# !/usr/bin/python3

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a, b)

print('a 和 b 的差集', a - b)  # bet 和 b 的差集
print('b 和 a 的差集', b - a)  # bet 和 b 的差集

print('a 和 b 的并集', a | b)  # bet 和 b 的并集

print('a 和 b 的交集', a & b)  # bet 和 b 的交集

print('a 和 b 的对称差', a ^ b)  # bet 和 b 中不同时存在的元素
