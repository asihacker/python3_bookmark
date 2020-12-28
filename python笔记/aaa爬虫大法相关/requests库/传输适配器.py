#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 21:22
# @Author  : AsiHacker
# @File    : 传输适配器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import requests
from requests.adapters import HTTPAdapter

# WARNING:urllib3.connectionpool:Connection pool is full, discarding connection: graph.facebook.com
# WARNING:urllib3.connectionpool:Connection pool is full, discarding connection: graph.facebook.com
# WARNING:urllib3.connectionpool:Connection pool is full, discarding connection: www.facebook.com
# WARNING:urllib3.connectionpool:Connection pool is full, discarding connection: www.facebook.com
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
session.mount('http://', adapter)
