#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 10:53
# @Author  : AsiHacker
# @File    : 提取关键词demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from googletrans import Translator

proxies = {'http': '127.0.0.1:1087'}
translate = Translator(service_urls=['translate.google.cn'])
result = translate.translate('照片')
print(result)
