#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 20:59
# @Author  : AsiHacker
# @File    : reversed-反转.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
a = reversed([1, 2, 3, 4, 5, 6, 3])
print(''.join([str(k) for k in a]))
a = reversed('123456')
print(''.join([str(k) for k in a]))
