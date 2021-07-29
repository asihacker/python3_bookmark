# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 14:11
# @Author  : AsiHacker
# @File    : redis生成者官
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 发布功能终端
import time

import redis

redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)
# 指定频道发送数据
i: int = 0
while 1:
    time.sleep(1)
    i += 1
    client.publish('fm87.7', f'send msg {i}')
    client.publish('fm87.8', f'send msg {i}')
    client.publish('fm87.9', f'send msg {i}')
