#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 10:20
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import urllib.request

rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
import chardet

print(chardet.detect(rawdata))
# 命令行工具 chardetect somefile someotherfile
