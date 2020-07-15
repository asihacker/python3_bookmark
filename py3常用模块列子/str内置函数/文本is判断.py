#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 22:35
# @Author  : AsiHacker
# @Site    : 
# @File    : 文本is判断.py
# @Software: PyCharm


# isalnum(): 检测字符串是否[只包含] 数字 + 字母( [@!111a] False [你a] True)
# isalpha(): 检测字符串是否[只包含] 中文 + 字母( [@!你a] False [你a] True)
# isascii():  是否为ascii码，判断时必须是字符串形式，或则报错
# isdecimal(): 可解释为十进制数字则返回True
# isdigit(): 是否全由数字组成，是则返回True
# isidentifier(): 用于判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法
# islower(): 判断字符串是否都是小写，是则返回True
# isnumeric(): 判断字符串是否只包含数字，是则返回True
# isprintable(): 判断字符串中所有字符是否都是可打印字符或字符串为空返回 True
# print('1aaa'.isalpha())
# print('11a11aa中'.isalnum())
