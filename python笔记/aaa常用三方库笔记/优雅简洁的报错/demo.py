#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 14:05
# @Author  : AsiHacker
# @File    : demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pretty_errors
if __name__ == '__main__':
    with open('status.json') as f:
        a = json.load(f)
    a['34eds']