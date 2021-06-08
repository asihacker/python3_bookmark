#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 16:36
# @Author  : AsiHacker
# @File    : zip_longest与zip相反.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

# 此方法提供的操作类似于zip()，与zip()不同的是，
# zip_longest()是以所有iterable中长度最长的那个为基准进行zip()操作，
# 遇到长度较短的iterable时，会以fillvalue（默认为None）指定的值去填充到相应的长度。
# 而zip会以短的哪个作为最大的迭代上限
print([i for i in itertools.zip_longest('ab', 'cdefg', 'xy', fillvalue='*')])
