#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 12:02
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 10:29
# @Author  : AsiHacker
# @File    : debug.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# 导入sympy
import time

from sympy import *

# 定义变量
x = Symbol('x')
y = Symbol('y')
t0 = time.perf_counter()
# x+y=10000
# x*1.05=y*1.06

print(solve([x + y - 10000, x * 1.05 - y * 1.06], [x, y]))
print(time.perf_counter() - t0)
