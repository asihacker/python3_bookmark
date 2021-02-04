#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:38
# @Author  : AsiHacker
# @File    : demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from cacheout import LRUCache

localCache = LRUCache(maxsize=9999)
localCache.set('a', '9128309')
print(localCache.get('a'))
