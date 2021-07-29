#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:49
# @Author  : AsiHacker
# @File    : compress迭代成员过滤.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

print(list(itertools.compress('abcdefg', [1, 2, 3, 1, 0, -1, 1])))  # 第2个参数放匿名函数也是可以的
# ps 布尔型变量bool的取值只有false和true，0为false，非0为true。（例如-1和1都是true）。
