#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:14
# @Author  : AsiHacker
# @File    : redis生产者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import json
import redis

# 以下代码是向redis 发命令
QUEUE = "code"  # 队列名称key

# redisPool = redis.ConnectionPool(host=config.get_redis_host(), port=6379, db=config.get_redis_db())
redisPool = redis.ConnectionPool(host='47.241.119.191', port=6379, db=11, password='nantian888')
client = redis.Redis(connection_pool=redisPool)


def send_cmd(seaweed):
    json_cmd = json.dumps(seaweed, ensure_ascii=False)
    client.rpush(QUEUE, json_cmd)


if __name__ == "__main__":
    ll = list(range(100))
    for k in ll:
        send_cmd({"label": k, 'timd': 20160503, 'timm': 20170430})
