#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 18:33
# @Author  : AsiHacker
# @Site    : 
# @File    : 翻墙.py
# @Software: PyCharm
# 动态转发通过参数 -D 指定，格式：-D [本地主机:]本地主机端口。相对于前两个来说，动态转发无需再指定远程主机及其端口。它们由通过 SOCKS协议
# 连接到本地主机端口的那个主机（peer，比如最常见的浏览器）指定（此属协议内容，无需深究）。
#
# 举例：ssh -D 50000 user@host。
