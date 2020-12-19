#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 14:30
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
from goose import Goose
from goose.text import StopWordsChinese

url = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print(article.cleaned_text[:150])
