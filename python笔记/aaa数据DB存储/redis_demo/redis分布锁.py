#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:35
# @Author  : AsiHacker
# @File    : redis分布锁.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# redis 锁
import time

import redis

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': '123456',
    'db': 8,
    'max_connections': 10,
}

connection_pool = redis.ConnectionPool(**redis_config)
redis = redis.StrictRedis(connection_pool=connection_pool)
lock = redis.lock(name='scheduler', timeout=60)
with lock:
    time.sleep(30)
    print(123)
