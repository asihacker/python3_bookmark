#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 19:43
# @Author  : AsiHacker
# @File    : chain串联小容器为大容器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import chain

a = [1, 3, 5, 0]
b = (2, 4, 6)

for i in chain(a, b):
    print(i)
