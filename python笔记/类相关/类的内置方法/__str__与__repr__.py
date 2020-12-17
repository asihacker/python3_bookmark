#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:16
# @Author  : AsiHacker
# @File    : __str__与__repr__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

class Test:
    def __str__(self):
        return "这是Test类"


f = Test()
print(f)

# __repr__(self)
# 与 __str__()类似 但是 与其不同的是__repr__()在解释器中触发，__str__()在print()中触发。　　返回的必须是字符串，否则会异常、
#
# print()函数只有当__str__()未定义。才会去调用__repr__()
