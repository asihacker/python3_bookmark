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
    'decode_responses': True  # 这样写取出的数据会有byte自动转化为字符串格式，但是部分用到redis的三方库，可能不兼容这个设置
}

# localCache = LRUCache(maxsize=9999)
connection_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=connection_pool)
# print(redis.incr(name='testincr'))
# print(redis.incr(name='testincr2'))
# print(redis.incr(name='testincr3'))
# del_list = ['testincr', 'testincr2', 'testincr3']
# print(redis.delete(*del_list))
# redis.set("ssr1", "1212414", ex=10)
# redis.set("ssr2", "34545", ex=10)
# print(redis.keys('ssr*'))
# for key in range(20):
#     time.sleep(1)
#     print(redis.keys('ssr*'))
lock = redis.lock(name='123123')
lock.acquire()
print(123)
lock.release()

print(lock.acquire())
print(123123)
lock.release()
