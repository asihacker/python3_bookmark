#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:30
# @Author  : AsiHacker
# @Site    : 
# @File    : 代理测试.py
# @Software: PyCharm
import requests

if __name__ == '__main__':
    proxies = {
        "https": "http://8.210.105.238:59394"
        # "http": "http://8.210.61.97:59394"
    }
    # rep = requests.get('https://www.baidu.com', proxies=proxies)
    # rep = requests.get('http://httpbin.org/get', proxies=proxies)
    rep = requests.get('https://www.facebook.com/', proxies=proxies)
    print(rep.text)
