#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 15:15
# @Author  : AsiHacker
# @File    : leetcode.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
name = '{wh}my \t name is {name},age is {age}.'
print(name.format_map({'wh': 'huanying,', 'name': 'xiaoming', "age": "19"}))
###########
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))
###########
print(dir(name))
