#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:17
# @Author  : AsiHacker
# @File    : redis-list模式-消费者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

import redis

QUEUE = "code"
redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)


def worker():
    while True:
        time.sleep(1)
        print(client.lpop(QUEUE))  # 如果queue没有数据则一直存在rpop的操作，这样对客户端的cpu消耗和redis性能的浪费


if __name__ == "__main__":
    # 多进程消费
    worker()
