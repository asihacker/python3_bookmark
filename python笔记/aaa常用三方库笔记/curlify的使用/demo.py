#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 14:17
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm
import curlify
import requests

if __name__ == '__main__':
    rsp = requests.get("https://www.baidu.com")
    print(curlify.to_curl(rsp.request))

