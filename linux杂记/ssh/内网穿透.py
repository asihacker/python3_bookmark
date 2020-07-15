#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:57
# @Author  : AsiHacker
# @Site    : 
# @File    : 内网穿透.py
# @Software: PyCharm

# 当成功执行上面的命令之后，访问登录主机的 8080 端口就相当于访问 localhost:80！

# ssh -R 8.210.18.224:39008:127.0.0.1:39003 root@8.210.18.224

# /etc/ssh/sshd_config 修改GatewayPorts 为 yes

# service sshd restart 重启ssh服务

# ssh -R 8.210.18.224:39008:127.0.0.1:39003 root@8.210.18.224 #再重新链接

