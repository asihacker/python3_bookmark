#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 16:33
# @Author  : AsiHacker
# @File    : tee生成相同的迭代对象.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

for tmp in [i for i in itertools.tee('ABCDEFG', 10)]:
    a = list(tmp)
    print(id(a), a)  # 这里是不同的对象哦，是deep copy
