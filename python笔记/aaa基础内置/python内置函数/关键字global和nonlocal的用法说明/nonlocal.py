#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 19:25
# @Author  : AsiHacker
# @File    : nonlocal.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
count = 12


def test():
    count = 10

    def test2():
        nonlocal count
        print(count)

    def test3():
        global count
        print(count)

    test2()
    test3()


if __name__ == '__main__':
    test()

