#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 20:46
# @Author  : AsiHacker
# @File    : 共享变量local.py
# @Software: PyCharm
import sys
import threading
from threading import local

data = local()
# 这个东西比全局变量来说
# 1.全局变量要加锁
# 这个东西比局部变量来说
# 1.别的地方引用这里的全局变量的话，对应线程会拿到对应的值
# 类似flask的request session的实现原理
# 可以理解为 一个全局的dict 用线程id为索引存储对应线程的值
