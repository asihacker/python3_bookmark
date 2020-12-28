#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 22:03
# @Author  : AsiHacker
# @File    : config.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import redis
from huey import RedisHuey

redis_config = {
    "host": '127.0.0.1',
    'port': 6379,
    'password': 'nantian888',
    'db': 8,
    'max_connections': 10,
    # 'decode_responses': True
}
connection_pool = redis.ConnectionPool(**redis_config)
huey = RedisHuey(connection_pool=connection_pool)
