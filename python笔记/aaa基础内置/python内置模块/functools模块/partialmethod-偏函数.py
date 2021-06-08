#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 21:26
# @Author  : AsiHacker
# @Site    : 
# @File    : partial-偏函数.py
# @Software: PyCharm
from functools import partialmethod


# 其实这个函数的作用就是：预先设置参数，使得之后调用的时候，减少函数的参数（也就是偏函数）

class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)  # 这里定义的是一个实例方法
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)

c.set_alive()
print(c.alive)
