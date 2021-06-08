#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 15:25
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from slugify import slugify

# https://github.com/voronind/awesome-slugify
# 应用场景：比如flask里面上传文件，对于一些文件的名称可以用这个库来处理
print(slugify('Any text'))
print(slugify('陈俊学'))
print(slugify('Asi*^Hac$%^ker', separator='*'))
print(slugify('18970084363.jpgj qkjwe'))
# to_lower              # 如果为True，则将文本转换为小写
# max_length            # 输出字符串最大长度
# separator             # 分隔符字符串
# capitalize            # 如果为真，则大写第一个字母
