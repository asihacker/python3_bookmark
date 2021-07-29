# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 14:09
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
def func():
    try:
        return 'try'
    finally:
        print('finally')


def func2():
    try:
        return 'try'
    finally:
        return 'finally'


if __name__ == '__main__':
    print(func())
    print(func2())
# 那结论就出来了，如果 finally 里有显式的 return，那么这个 return 会直接覆盖 try 里的 return，
# 而如果 finally 里没有 显式的 return，那么 try 里的 return 仍然有效。
