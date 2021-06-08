#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 22:12
# @Author  : AsiHacker
# @File    : Parameter-构建入参（很少用）.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from inspect import Parameter, signature


def foo(a=1):
    print(a)
    return

param = Parameter('c', Parameter.KEYWORD_ONLY, default=20)
param = str(param)
a = foo(param)  # 详单于 foo(bet='20')
