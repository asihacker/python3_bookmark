#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:22
# @Author  : AsiHacker
# @Site    : 
# @File    : celeryconfig.py.py
# @Software: PyCharm
BROKER_URL = 'redis://:nantian888@127.0.0.1:6379/1'  # 使用Redis作为消息代理

CELERY_RESULT_BACKEND = 'redis://:nantian888@127.0.0.1:6379/2'  # 把任务结果存在了Redis

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型
