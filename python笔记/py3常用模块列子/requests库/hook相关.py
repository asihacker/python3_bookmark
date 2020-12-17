#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 12:01
# @Author  : AsiHacker
# @File    : hook相关.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# from requests import Session
# from requests import Request
#
#
# class AsiSession(Session):
#     def get(self, *args, **kwargs):
#         rsp = super().request(*args, **kwargs)
#         self.cookies = rsp.cookies
#         return rsp
#
#     def __setattr__(self, key, value):
#         print('----> from setattr')
#         self.__dict__[key] = value  # 应该使用它
#         print(key, value)
#
#
# a = AsiSession()
# rsp = a.get(method='GET', url='http://www.baidu.com')
# print(rsp)
import requests
import curlify


def get_key(response, *args, **kwargs):
    print(response.headers['Content-Type'])


def get_cookies(response, *args, **kwargs):
    print(response.cookies)


def get_curl(response, *args, **kwargs):
    print(curlify.to_curl(response.request))


def myresponse():
    url = "https://www.baidu.com"
    requests.get(url, hooks=dict(response=[get_key, get_cookies, get_curl]))


myresponse()
