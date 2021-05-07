#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:17
# @Author  : AsiHacker
# @File    : redis消费者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import json

import chardet  # 还包含一个命令行工具chardetect xx.txt |或者输入字符串然后ctrl + D
import redis

# 以下代码是向redis 发命令
QUEUE = "code"
# redisPool = redis.ConnectionPool(host=config.get_redis_host(), port=6379, db=config.get_redis_db())
redisPool = redis.ConnectionPool(host='47.241.119.191', port=6379, db=11, password='nantian888')
client = redis.Redis(connection_pool=redisPool)


# 以下代码是向redis 取命令，并且采用多进程来实现计算
def func(a, b, c):
    print(a, b)


def worker():
    client = redis.Redis(connection_pool=redisPool)
    while True:
        try:
            cmd = client.lpop(QUEUE)
            encode1 = chardet.detect(cmd)["encoding"]
            cmd = cmd.decode(encode1)
        except:
            cmd = None
        if cmd is None:
            print('没有啦')
        else:
            cmd = format_cmd(cmd)
            print(cmd)


def format_cmd(cmd):
    return json.loads(cmd)


if __name__ == "__main__":
    # 多进程消费
    worker()
