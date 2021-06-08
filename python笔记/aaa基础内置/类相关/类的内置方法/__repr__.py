#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:49
# @Author  : AsiHacker
# @File    : __repr__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"

    def __repr__(self):
        return "CLanguage[name=" + self.name + ",add=" + self.add + "]"


clangs = CLanguage()
print(clangs)
