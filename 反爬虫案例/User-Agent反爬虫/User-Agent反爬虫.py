#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 11:24
# @Author  : AsiHacker
# @Site    : 
# @File    : User-Agent反爬虫.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

r = requests.get('http://localhost:8205/verify/uas/index.html', headers=headers)
# r = requests.get('http://localhost:8205/verify/uas/index.html')#403

a = BeautifulSoup(r.text, 'html.parser')
print(a.prettify())
c = a.find_all('h4')
for key in c:
    print(key.find('a').get_text())
