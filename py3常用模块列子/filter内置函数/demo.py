#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 09:39
# @Author  : AsiHacker
# @Site    : 
# @File    : dataclass模块.py
# @Software: PyCharm
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
