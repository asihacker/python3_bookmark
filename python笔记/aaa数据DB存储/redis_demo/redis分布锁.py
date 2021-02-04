#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:35
# @Author  : AsiHacker
# @File    : redis分布锁.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# redis 锁
import redis

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': 'nantian888',
    'db': 8,
    'max_connections': 10,
}


connection_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=connection_pool)
lock = redis.lock(name='123123')
lock.acquire()
print(123)
lock.release()

print(lock.acquire())
print(123123)
lock.release()
