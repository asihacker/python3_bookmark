#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:32
# @Author  : AsiHacker
# @Site    : 
# @File    : redis_demo.py
# @Software: PyCharm
import json
import time

import redis
from cacheout import LRUCache

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': 'nantian888',
    'db': 8,
    'max_connections': 10,
    'decode_responses': True
}

# localCache = LRUCache(maxsize=9999)
_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=_pool)
redis.set("ssr1", "1212414", ex=10)
redis.set("ssr2", "34545", ex=10)
print(redis.keys('ssr*'))
for key in range(20):
    time.sleep(1)
    print(redis.keys('ssr*'))
