#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 21:14
# @Author  : AsiHacker
# @File    : filter-过滤函数.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import string


def filter_num(d_str: str):
    """
    获取文本中的数字
    :param d_str:
    :return:
    """
    num = filter(str.isdigit, d_str)
    return ''.join(num)


def filter_alp(d_str: str):
    """
    过滤文本中的字母
    :param d_str:
    :return:
    """
    alp = list(filter(lambda d: d in string.ascii_letters, d_str))
    print(alp)


import string

a = 'a1b2c3d4e5f6g7'
# '1234567'
b = ''.join(list(filter(lambda _: _ in string.digits, a)))
print(b)
b = ''.join([key for key in a if key in string.digits])
print(b)
import re

b = ''.join(re.findall(r'\d', a))
