#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 00:51
# @Author  : AsiHacker
# @File    : UserString省内存的string.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from collections import UserString

d0 = 'asihacker'
d1 = UserString(d0)
import sys

print(sys.getsizeof(d0))
print(sys.getsizeof(d1))
print(type(d1.data))
