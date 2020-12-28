#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:45
# @Author  : AsiHacker
# @File    : chain.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

for c in itertools.chain('ABC', 'XYZ'):  # 可以把一组迭代对象串联起来，形成一个更大的迭代器
    print(c)
