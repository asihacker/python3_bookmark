#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:32
# @Author  : AsiHacker
# @Site    : 
# @File    : redis集群连接.py
# @Software: PyCharm

redis = RedisCluster(startup_nodes=redis_cluster_config, decode_responses=True, password='nantian',
                     max_connections=100)