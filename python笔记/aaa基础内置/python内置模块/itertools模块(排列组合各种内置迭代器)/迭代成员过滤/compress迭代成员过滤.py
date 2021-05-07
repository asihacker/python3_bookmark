#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:49
# @Author  : AsiHacker
# @File    : compress迭代成员过滤.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

print([i for i in itertools.compress('ABCDEFG', 'You Need Python')])
"""
个人理解：这里我们可以实现这样一个操作，传入两个iterable作为compress的参数，其中selectors是过滤器，
data是我们传入的原始待处理的数据，compress的结果就是data与selectors的元素一一对应，判断selectors的元素是否为True，
是即保留对应data的元素，否则舍弃掉对应data的元素。
"""
