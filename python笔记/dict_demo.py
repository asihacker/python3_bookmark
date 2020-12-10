#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 14:35
# @Author  : AsiHacker
# @File    : dict_demo.py
# @Software: PyCharm
a = {'a': 1, 'b': 2, 'c': 3}
print(a.get('a', None))
print(a.setdefault('d', 6))
print(a)
