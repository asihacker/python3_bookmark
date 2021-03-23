#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 15:09
# @Author  : AsiHacker
# @File    : 计算器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s)


if __name__ == '__main__':
    print(eval('2-1+2'))
