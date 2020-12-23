#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 11:16
# @Author  : AsiHacker
# @Site    : 
# @File    : dataclass模块.py
# @Software: PyCharm
import random

from fake_useragent import UserAgent

ua = UserAgent()


# print(ua.safari)

for k in range(1000):
    print(ua.chrome)
# print(ua.msie)
# print(ua.opera)
# print(ua.chrome)
# print(ua.google)
# print(ua.firefox)
# print(ua.ff)
# print(ua.safari)
# print(ua.random)


# def get_rondom_user_agent():
#     random.seed()
#     ua = UserAgent()
#     ua_type = ['ie', 'chrome', 'safari', 'google']
#     UA = getattr(ua, random.choice(ua_type))
#     return UA
#
#
# if __name__ == '__main__':
#     print(get_rondom_user_agent())
