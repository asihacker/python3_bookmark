#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 21:18
# @Author  : AsiHacker
# @File    : stack-栈与帧.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import inspect
import pprint


def show_stack():
    for level in inspect.stack():
        print("{}[{}]\n -> {}".format(level.frame.f_code.co_filename,
                                      level.lineno,
                                      level.code_context[level.index].strip()))
        pprint.pprint(level.frame.f_locals)
        print("\n")


def recurse(limit):
    local_variable = "." * limit
    if limit <= 0:
        show_stack()
        return
    recurse(limit - 1)
    return local_variable


if __name__ == '__main__':
    recurse(2)
