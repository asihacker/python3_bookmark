#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:32
# @Author  : AsiHacker
# @Site    : 
# @File    : redis连接.py
# @Software: PyCharm

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
