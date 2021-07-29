# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 16:22
# @Author  : AsiHacker
# @File    : redis-订阅发布模式线程-消费者.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import redis

redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11, password='123456')
client = redis.Redis(connection_pool=redisPool)
# 打开订阅功能
sub = client.pubsub()
# 声明订阅的频道
sub.subscribe('fm87.7', 'fm87.8', 'fm87.9')


def my_handler(message):
    print(message)


sub.subscribe(**{'fm87.7': my_handler, 'fm87.8': my_handler, 'fm87.9': my_handler})
# sub.psubscribe('fm*')  # 正则的方式订阅
# 开始订阅,第一次会返回一条订阅信息，第二次开始持续订阅

sub.run_in_thread()
