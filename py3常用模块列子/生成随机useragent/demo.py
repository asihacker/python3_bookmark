#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 11:16
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)
print(ua.msie)
print(ua.opera)
print(ua.chrome)
print(ua.google)
print(ua.firefox)
print(ua.ff)
print(ua.safari)
print(ua.random)
