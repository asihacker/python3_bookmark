#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:32
# @Author  : AsiHacker
# @Site    : 
# @File    : redis_demo.py
# @Software: PyCharm
import json

import redis
from cacheout import LRUCache

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': '123456',
    'db': 8,
    'max_connections': 10,
    'decode_responses': True
}

# localCache = LRUCache(maxsize=9999)
_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=_pool)
