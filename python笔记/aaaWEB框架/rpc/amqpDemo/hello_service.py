#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:01
# @Author  : AsiHacker
# @File    : hello_service.py.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.


from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

# 启动命令
# nameko run hello_service:GreetingService  --broker amqp://asi:asi@127.0.0.1
# nameko shell --broker amqp://asi:asi@127.0.0.1
# n.rpc.greeting_service.hello(name="123🚗")
