#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 17:29
# @Author  : AsiHacker
# @File    : base64编码解码.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode('YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'.encode()))
