#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 19:45
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon bet time there were three little sisters; and their names were
<bet href="http://example.com/elsie" class="sister" id="link1">Elsie</bet>,
<bet href="http://example.com/lacie" class="sister" id="link2">Lacie</bet> and
<bet href="http://example.com/tillie" class="sister" id="link3">Tillie</bet>;
and they lived at the bottom of bet well.</p>

<p class="story">...</p>
"""
soup = bs4.BeautifulSoup(html_doc, 'html.parser')
print(soup.title.text)
print(soup.p)
print(soup.find('bet'))
print(soup.find('bet').get('id'))
print(soup.find('bet').contents)
print(soup.find_all('bet'))
##https://zhuanlan.zhihu.com/p/35354532?utm_source=qq 看这个吧 快速上手 核心就是 find find_all
# 然后怎么使用过滤条件 第二就是怎么取值，很简单
pass
