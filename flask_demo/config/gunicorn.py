#!/usr/bin/python
# coding=utf-8
# config.py
"""
http://docs.gunicorn.org/en/stable/index.html
https://www.jianshu.com/p/29467ce73972
https://www.jianshu.com/p/260f18aa5462
https://www.jianshu.com/p/6fc90cee7252
"""
"""
-c CONFIG, --config=CONFIG-形式指定一个配置文件 $(PATH)，file:$(PATH)或python:$(MODULE_NAME)。
-b BIND, --bind=BIND-指定要绑定的服务器套接字。服务器插槽可以是任意的$(HOST)，$(HOST):$(PORT)，fd://$(FD)，或 unix:$(PATH)。IP是有效的$(HOST)。
-w WORKERS, --workers=WORKERS-工作进程数。此数字通常应在服务器中每个核心2-4个工作线程之间。检查常见问题，以获取有关调整此参数的想法。
-k WORKERCLASS, --worker-class=WORKERCLASS-要运行的工作进程的类型。您肯定要阅读生产页面，以了解此参数的含义。您可以设置这$(NAME) 其中$(NAME)的一个sync，eventlet，gevent， tornado，gthread。 sync是默认值。有关更多信息，请参见worker_class文档。
-n APP_NAME, --name=APP_NAME-如果安装了setproctitle，则可以调整Gunicorn进程在进程系统表中显示的名称（这会影响诸如ps和的工具top）。
"""
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

debug = True
loglevel = 'debug'
bind = "0.0.0.0:8000"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = False

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
