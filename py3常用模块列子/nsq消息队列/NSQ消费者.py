#!/usr/bin/python
# coding=utf-8
import nsq


def handler(message):
    print(message.body)
    return True


r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['nsq.fqwang.net:4150'],
               topic='asi_debug',
               channel='asi',
               lookupd_poll_interval=15)

nsq.run()  # tornado.ioloop.IOLoop.instance().start()
