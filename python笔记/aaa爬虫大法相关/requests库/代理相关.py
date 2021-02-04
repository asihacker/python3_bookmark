#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 15:13
# @Author  : AsiHacker
# @File    : 代理相关.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import requests

session = requests.session()
# 213.166.94.9:52055:VXaYth95:p9eKfJQW:s5
# {"host":"213.139.195.40","port":"53396","type":"http","user":"9YSyB1CA","pass":"RrqnFsgS"}
session.proxies = {'http': 'http://9YSyB1CA:RrqnFsgS@213.139.195.40:53396',
                   'https': 'https://9YSyB1CA:RrqnFsgS@213.139.195.40:53396'}

# session.proxies = {'http': 'http://127.0.0.1:1087',
#                    'https': 'http://127.0.0.1:1087'}
rsp = session.get('https://httpbin.org/get')
print(rsp.json())
