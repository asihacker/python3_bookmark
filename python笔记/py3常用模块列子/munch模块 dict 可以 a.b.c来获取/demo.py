#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 16:57
# @Author  : AsiHacker
# @File    : demo.py
# @Software: PyCharm
from munch import Munch

if __name__ == '__main__':
    data = {'a': {'b': {'c': [1, 2, 3, 4]}}}
    data = Munch.fromDict(data)
    print(data.a.b.c)
