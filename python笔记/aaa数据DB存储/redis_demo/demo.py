#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 17:06
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import json

import redis as redis

redis_config = {
    "host": '47.115.20.50',
    'port': 6379,
    'password': 'nantian888',
    'db': 1,
    'max_connections': 10,
    'decode_responses': True  # 这样写取出的数据会有byte自动转化为字符串格式，但是部分用到redis的三方库，可能不兼容这个设置
    # 对象不可以设置为真
}

# localCache = LRUCache(maxsize=9999)
connection_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=connection_pool)
keys = redis.keys(r'account_list:*')
redis.zpopmin()
a = """
119.23.47.183:59394
120.77.245.105:59394
119.23.232.165:59394
112.74.175.231:59394
112.74.187.0:59394"""
c = a.split()
for k in keys:
    if json.loads(redis.get(k))["proxy"] in c:
        print(k)
    else:
        redis.delete(k)
