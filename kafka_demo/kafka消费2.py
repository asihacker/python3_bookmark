#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 16:51
# @Author  : AsiHacker
# @Site    : 
# @File    : kafka消费2.py
# @Software: PyCharm
from kafka import KafkaConsumer

consumer = KafkaConsumer('cloud_python', group_id='group_xiaochen', client_id='client_asi1',
                         bootstrap_servers=['47.112.163.25:9092', '47.112.185.243:9092', '47.112.189.251:9092'])
print(consumer)
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)

"""
kafka集群地址：47.112.163.25:9092,47.112.185.243:9092,47.112.189.251:9092
测试主题名：textMsg
"""
