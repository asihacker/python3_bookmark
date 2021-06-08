#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 09:59
# @Author  : AsiHacker
# @File    : all与any.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true

# all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False

a = [1, 0]
print(all(a))
print(any(a))
