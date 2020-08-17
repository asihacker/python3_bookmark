#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 09:39
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
def filter_num(d_str: str):
    """
    获取文本中的数字
    :param d_str:
    :return:
    """
    num = filter(str.isdigit, d_str)
    return ''.join(num)
