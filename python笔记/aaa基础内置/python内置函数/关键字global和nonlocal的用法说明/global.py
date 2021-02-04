#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 18:27
# @Author  : AsiHacker
# @File    : global.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

count = 10


# 如果局部不声明全局变量，并且不修改全局变量，则可以正常使用。
def test():
    print(count)


# 如果局部要对全局变量修改，应在局部声明该全局变量
def test2():
    count = 12
    print(count)


if __name__ == '__main__':
    test()
    test2()
