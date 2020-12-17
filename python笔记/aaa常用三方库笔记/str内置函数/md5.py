#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 09:22
# @Author  : AsiHacker
# @Site    : 
# @File    : md5.py
# @Software: PyCharm
if __name__ == '__main__':
    a = '1289uiuwefbisbcbab'
    import hashlib

    print(hashlib.md5(a.encode()).hexdigest())
