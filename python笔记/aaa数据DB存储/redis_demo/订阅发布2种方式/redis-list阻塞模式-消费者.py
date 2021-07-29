# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 14:41
# @Author  : AsiHacker
# @File    : redis-list阻塞模式-消费者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

import redis

QUEUE = "code"
redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)


def worker():
    while True:
        print(client.blpop(QUEUE, timeout=30))  # timeout=0 则无限阻塞 30则30秒后则返回None,对比 lpop 优势是消费基本没有延迟


if __name__ == "__main__":
    # 多进程消费
    worker()
