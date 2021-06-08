#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 00:48
# @Author  : AsiHacker
# @File    : UserDict省内存的dict.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from collections import UserDict

d0 = dict(a=1, b=2)
d1 = UserDict(d0)
import sys

print(sys.getsizeof(d0))
print(sys.getsizeof(d1))
print(d1.data)
