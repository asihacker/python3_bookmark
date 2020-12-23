#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 19:13
# @Author  : AsiHacker
# @File    : websocket-server-demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import asyncio

import click
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """
    doc
    """
    c = set()

    def check_origin(self, origin):
        """
        检查来源默认为TRUE，后期可以在这里做验权
        :param origin:
        :return:
        """
        return True

    def open(self):
        """
        客户端链接
        :return:
        """
        WebSocketHandler.c.add(self.request.server_connection.context.address[1])
        print('客户进入', self.request.server_connection.context.address[1], len(WebSocketHandler.c))

    def on_message(self, message):
        """
        收到消息
        :param message:
        :return:
        """
        print("收到消息", message)
        self.write_message(message)

    def on_close(self):
        """
        客户端断开事件
        :return:
        """
        print('客户离开', self.request.host)
        WebSocketHandler.c.remove(self.request.server_connection.context.address[1])
        print('客户离开', self.request.host, len(WebSocketHandler.c))


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', WebSocketHandler)
        ]
        settings = {
            'template_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


@click.command()
@click.option('-p', default=9898, help='运行端口')
def websocket_port(p: int):
    """
    开启web服务器
    :param p: web端口
    :return:
    """
    asyncio.set_event_loop(asyncio.new_event_loop())
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(p, "0.0.0.0")
    print('ws', f"0.0.0.0:{p}")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    websocket_port()
