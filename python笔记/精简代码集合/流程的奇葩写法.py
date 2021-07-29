#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 14:25
# @Author  : AsiHacker
# @File    : 流程的奇葩写法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
age = 100
msg = age > 18 and '成年' or '未成年'  # 其实就是 msg = （age > 18 and '成年'） or '未成年'
print(msg)
# 下面3钟都是一类写法了 True=1 False=0
msg = ('成年', '未成年')[age < 18]
print(msg)
msg = ['成年', '未成年'][age < 18]
print(msg)
msg = {True: '成年', False: '未成年'}[age > 18]
print(msg)
