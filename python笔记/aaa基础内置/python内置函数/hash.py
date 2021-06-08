#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 23:11
# @Author  : AsiHacker
# @Site    : 
# @File    : hash.py
# @Software: PyCharm
print(hash(123123))
print(hash('123123'))  # 字符串同进程下 hash一致 ，不同进程hash不一致
print(hash('123123'))
print(hash('123123'))
print(hash('123123'))
print(id('123123'))


class Apple(object):
    def test(self):
        return


print(hash(Apple))
