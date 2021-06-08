#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 16:32
# @Author  : AsiHacker
# @File    : starmap函数.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

# 类似map
print([i for i in itertools.starmap(pow, [(2, 5), (5, 2), (10, 3)])])
