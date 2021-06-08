#!/usr/bin/python
# coding=utf-8
import json

import nsq
import requests


def handler(message):
    print(message.body)
    # print(json.loads(message.body.decode()))
    rsp = requests.post('http://fbchat.xyz:39002/api/mail/web_hook', data=message.body)
    print(rsp.text)
    b = json.loads(message.body.decode().split('\r\n\r\n')[1].split('\r\n----------------------------')[0])
    print(b)
    return True


# r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['nsq.fqwang.net:4150'],
#                topic='asi_debug',
#                channel='asi',
#                lookupd_poll_interval=15)

r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['fbchat.xyz:4150'],
               topic='email',
               channel='asi',
               lookupd_poll_interval=15)

nsq.run()  # tornado.ioloop.IOLoop.instance().start()
