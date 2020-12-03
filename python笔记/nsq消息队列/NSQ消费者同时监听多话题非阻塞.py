#!/usr/bin/python
# coding=utf-8
import nsq
import tornado.ioloop
import threading


def handler(message):
    data = str(message.body, 'utf-8')
    print(data)


def handler2(message):
    data = str(message.body, 'utf-8')
    print(data)


def starnsq():
    """
    开始监听nsq
    :return:
    """

    nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['nsq.fqwang.net:4150'],
               topic='asi_debug',
               channel='asi',
               lookupd_poll_interval=15)

    nsq.Reader(message_handler=handler2, nsqd_tcp_addresses=['nsq.fqwang.net:4150'],
               topic='dsqUpdateFriendFormal',
               channel='asi_debug2',
               lookupd_poll_interval=15)
    tornado.ioloop.IOLoop.instance().start()  # 这里可以串联多个loop事件，比如websocket的listen


if __name__ == '__main__':
    threading.Thread(target=starnsq).start()
