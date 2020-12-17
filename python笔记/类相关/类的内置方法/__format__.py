#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:17
# @Author  : AsiHacker
# @File    : __format__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Date:

    def __init__(self, year, mon, day):
        self.y = year
        self.m = mon
        self.d = day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in format_dict:  # 如果没有指定format_spec 或者不存在的格式就默认给他ymd格式
            format_spec = 'ymd'
        fmt = format_dict[format_spec]
        return fmt.format(self)


d = Date("2018", "4", "9")
print(format(d))
print(format(d, 'y-m-d'))
print(format(d, 'm-d-y'))
