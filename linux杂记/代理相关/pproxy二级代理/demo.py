#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 17:15
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
"""
  -h, --help        显示此帮助消息并退出
  -l LISTEN         tcp服务器uri（默认值：http+socks4+socks5://：8080/）
  -r RSERVER        tcp远程服务器uri（默认值：直接）
  -ul ULISTEN       udp服务器设置uri（默认值：无）
  -ur URSERVER      udp远程服务器uri（默认值：直接）
  -b BLOCK          阻止正则表达式规则
  -a ALIVED         检查远程活动的间隔（默认值：无检查）
  -s {fa,rr,rc,lc}  调度算法（默认：第一个可用）
  -d                启用“调试”以查看回溯（默认值：无调试）
  -v                打印详细输出
  --ssl SSLFILE     certfile[，keyfile]如果服务器在ssl模式下侦听
  --pac PAC         http PAC路径
  --get GETS        http自定义{路径，文件}
  --auth AUTHTIME   同一ip的重新验证时间间隔（默认值：86400*30）
  --sys             更改系统代理设置（mac、windows）
  --reuse           设置SO\u重用端口（仅限Linux）
  --daemon          作为守护程序运行（仅限Linux）
  --test TEST       为所有远程代理测试此url并退出
  --version         显示程序的版本号并退出

"""
# https://github.com/qwj/python-proxy
# 开启二级代理
# pproxy -r http://username:password@IP:port
# pproxy -r socks5://username:password@IP:port
# pproxy -r http://139.180.129.221:59394 -l  http+socks4+socks5://:9898/ -vv
# 还支持ssr 具体看git
