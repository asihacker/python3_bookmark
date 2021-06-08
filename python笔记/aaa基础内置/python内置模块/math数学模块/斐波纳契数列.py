#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:48
# @Author  : AsiHacker
# @File    : 斐波纳契数列.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
fibo = [0, 1]
print([fibo.append(fibo[-2] + fibo[-1]) for i in range(5)])
