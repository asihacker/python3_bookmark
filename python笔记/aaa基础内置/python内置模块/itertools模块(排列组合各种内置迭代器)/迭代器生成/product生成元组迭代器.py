#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:23
# @Author  : AsiHacker
# @File    : product生成元组迭代器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

itertools.product([1, 2, 3], [100, 200])
for item in itertools.product([1, 2, 3], [100, 200]):
    print(item)
itertools.starmap()
