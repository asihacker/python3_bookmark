#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:01
# @Author  : AsiHacker
# @File    : service.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://asi:asi@127.0.0.1"}


def compute():
    with ClusterRpcProxy(CONFIG) as rpc:
        a = rpc.hello_service.hello()


if __name__ == '__main__':
    compute()
