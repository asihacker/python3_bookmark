#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:14
# @Author  : AsiHacker
# @File    : redis-list模式-生产者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

import redis

QUEUE = "code"  # 队列名称key

redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)

if __name__ == "__main__":
    i: int = 0
    while 1:
        time.sleep(1)
        i += 1
        print(client.rpush(QUEUE, f'send msg {i}'))
