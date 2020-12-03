#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 12:36
# @Author  : AsiHacker
# @File    : demo.py
# @Software: PyCharm
# crontab命令还有一些其他的选项
#
# 　　-u #指定哪个用户的cron服务，一般是root用户执行这个命令的时候需要
#
# 　　-l #列出用户的定时任务列表，默认当前用户
#
# 　　-r #删除用户的定时任务列表，默认当前用户
#
# 　　-e #编辑用户的定时任务列表，默认当前用户

# 快速编辑crontab技巧
# crontab -l > crontab
#
# echo "* * * * *  source ~/.bash_profile;"  >> crontab
#
# crontab crontab
