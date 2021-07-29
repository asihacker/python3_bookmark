#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:34
# @Author  : AsiHacker
# @File    : redis保存对象.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pickle

import redis

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': 'nantian888',
    'db': 8,
    'max_connections': 10,
    # 'decode_responses': True  # 这样写取出的数据会有byte自动转化为字符串格式，但是部分用到redis的三方库，可能不兼容这个设置
    # 对象不可以设置为真
}

# localCache = LRUCache(maxsize=9999)
connection_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=connection_pool)


# redis存储对象
class ExampleObject:
    def __init__(self, a: str):
        self.a = a


obj = ExampleObject(a='3')
pickled_object = pickle.dumps(obj)
redis.set('some_key', pickled_object)
unpacked_object = pickle.loads(redis.get('some_key'))
print(unpacked_object == obj)
redis.expire()