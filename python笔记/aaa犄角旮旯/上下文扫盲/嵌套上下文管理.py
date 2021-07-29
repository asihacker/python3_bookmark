# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:32
# @Author  : AsiHacker
# @File    : 嵌套上下文管理
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import contextlib


@contextlib.contextmanager
def test_context(name):
    print('enter, my name is {}'.format(name))

    yield

    print('exit, my name is {}'.format(name))


# 方法一
with test_context('aaa'):
    with test_context('bbb'):
        print('========== in main ============')
# 方法二
with test_context('aaa'), test_context('bbb'):
    print('========== in main ============')
