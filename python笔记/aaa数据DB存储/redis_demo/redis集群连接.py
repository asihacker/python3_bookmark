#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:32
# @Author  : AsiHacker
# @Site    : 
# @File    : redis集群连接.py
# @Software: PyCharm
# redis-py-cluster==2.1.3 请使用这个版本 redis 3.5.3
from rediscluster import RedisCluster

redis_cluster_config = [
    {'host': '8.129.210.253', 'port': '6379'},
    {'host': '8.129.187.90', 'port': '6379'},
    {'host': '8.129.173.151', 'port': '6379'},
    {'host': '47.113.91.118', 'port': '6379'},
    {'host': '39.108.255.150', 'port': '6379'},
    {'host': '8.129.211.201', 'port': '6379'}
]
r = RedisCluster(startup_nodes=redis_cluster_config, decode_responses=True, password='nantian',
                 max_connections=100)
print(r.ping())
print(r.ping())
print(r.ping())
print(r.ping())
print(r.ping())
