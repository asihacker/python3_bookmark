# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 11:07
# @Author  : AsiHacker
# @File    : ddemo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from contextlib import contextmanager


@contextmanager
def make_context():
    print('1')
    try:
        yield {}
        print(2)
    except RuntimeError as err:
        print('error', err)
    finally:
        print('4')


with make_context() as value:
    print(3)
    print(value)
