#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 00:50
# @Author  : AsiHacker
# @File    : UserList省内存的list.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from collections import UserList

d0 = [1, 2, 3]
d1 = UserList(d0)
import sys

print(sys.getsizeof(d0))
print(sys.getsizeof(d1))
print(d1.data)
