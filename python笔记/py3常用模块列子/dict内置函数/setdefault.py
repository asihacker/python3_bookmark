#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 21:47
# @Author  : AsiHacker
# @File    : setdefault.py
# @Software: PyCharm
a = {'a': 1}
print(a.setdefault('b', []).append(23))  # 字典里面没有 则设置 【】 ，并且返回 【】，所以可以用append
print(a)
