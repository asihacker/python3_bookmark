#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 18:18
# @Author  : AsiHacker
# @File    : 等分数组.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
other = range(500)
step = 50
iter_other = [other[i:i + step] for i in range(0, len(other), step)]
print(iter_other)
