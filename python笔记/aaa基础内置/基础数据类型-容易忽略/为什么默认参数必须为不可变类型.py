#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 21:48
# @Author  : AsiHacker
# @File    : 为什么默认参数必须为不可变类型.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
def addend(lt=[]):
    lt.append('end')
    return lt


# 传入一个普通的列表，输出结果正确
lst = [1, 2, 3, 4]
print(addend(lst))

# 不传入任何参数，第二次调用，多输出了一个'end'
print(addend())
print(addend())