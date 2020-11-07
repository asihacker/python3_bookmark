#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 12:23
# @Author  : AsiHacker
# @Site    : 
# @File    : Cookie 反爬虫.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

headers = {
    'cookie': 'isfirst=789kq7uc1pp4c'
}
rsp = requests.get('http://localhost:8207/verify/cookie/content.html', headers=headers)
cookies = rsp.cookies
print(rsp.status_code)
print(rsp.text)
c = BeautifulSoup(rsp.text, 'html.parser')
d = c.find_all('p')
for k in d:
    print(k.get_text())
# 使用session自动维系cookies
# session = requests.session()
# rsp = session.get('http://localhost:8207/verify/cookie/index.html')
# rsp = session.get('http://localhost:8207/verify/cookie/content.html')
# print(rsp.text)
