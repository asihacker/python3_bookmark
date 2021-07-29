# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 14:11
# @Author  : AsiHacker
# @File    : redis消费者官
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import redis

redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)
# 打开订阅功能
sub = client.pubsub()
# 声明订阅的频道
sub.subscribe('fm87.7', 'fm87.8', 'fm87.9')
# sub.psubscribe('fm*')  # 正则的方式订阅
# 开始订阅,第一次会返回一条订阅信息，第二次开始持续订阅
sub.handle_message()
while 1:
    print(sub.parse_response())