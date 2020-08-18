#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 09:53
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
from dataclasses import dataclass


# 可以省略def __init__()
# 可以Apple().kg
@dataclass
class Apple(object):
    """
    123123
    """
    kg: int = 11
    color: str = 'red'
    size: int = 13


if __name__ == '__main__':
    aaa = Apple(kg=17, color='greed', size=90)
    print(aaa.kg)
    print(getattr(aaa, 'kg'))
    print(delattr(aaa, 'kg'))
    print(getattr(aaa, 'kg'))
    print(aaa.kg)
    aaa.kg = 'asi'
    print(aaa.kg)

