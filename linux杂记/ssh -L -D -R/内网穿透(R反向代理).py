#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:57
# @Author  : AsiHacker
# @Site    : 
# @File    : 内网穿透(R反向代理).py
# @Software: PyCharm
# https://zhuanlan.zhihu.com/p/57630633
# 当成功执行下面的命令之后，访问登录主机的 39008 端口就相当于访问 localhost:39003！

# ssh -R 8.210.18.224:39008:127.0.0.1:39003 root@8.210.18.224

# 服务器需要进行下面配置

# /etc/ssh/sshd_config 修改GatewayPorts 为 yes

# service sshd restart 重启ssh服务

# ssh R 8.210.18.224:39008:127.0.0.1:39003 root@8.210.18.224 #再重新链接
