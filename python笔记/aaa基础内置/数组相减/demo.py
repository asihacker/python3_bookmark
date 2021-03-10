#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 20:01
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import re

if __name__ == '__main__':
    a = re.findall(r'^[0-9]*$', '123019230912390')
    print(a)
    aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bb = [2, 4, 6, 8]
    print(set(aa) - set(bb))
    print(aa + bb)
    print(aa.extend(bb))
    print(aa)
    aaa = [[1], [2], [1, 2, 3, 4]]
    bbb = [5, 6, 7, 8]
    print(aaa + bbb)
    print(bbb.extend(aaa))
    print(bbb)
