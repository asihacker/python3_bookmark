#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 14:45
# @Author  : AsiHacker
# @File    : range-基础类型范围.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
a = range(3)
for k in a:
    print(k)
print('---------')
b = range(3, 8, 2)  # 3个参数分别是 开始 3 ｜ 停止 8｜步长 2
for k in b:
    print(k)
