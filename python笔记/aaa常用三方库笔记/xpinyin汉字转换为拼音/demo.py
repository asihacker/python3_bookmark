#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 11:24
# @Author  : AsiHacker
# @File    : demo.txt.txt-svg.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from xpinyin import Pinyin

# https://github.com/lxneng/xpinyin
p = Pinyin()
print(p.get_pinyin("上海"))
print(p.get_pinyin("上海", tone_marks='marks'))
print(p.get_pinyin("上海", tone_marks='numbers'))
