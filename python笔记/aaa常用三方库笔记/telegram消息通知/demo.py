#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 23:45
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import telegram
from telegram.ext import Updater

TOKEN = '1503342956:AAEVHa4OWJFuUpwSfRKdApXdZnTjxZsMvjo'
REQUEST_KWARGS = {
    # "USERNAME:PASSWORD@" is optional, if you need authentication:
    'proxy_url': 'http://127.0.0.1:1087',
}

updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
bot = updater.bot
print(bot.get_me())
a = bot.getUpdates()  # 获取chat_id列表
print(bot.send_message(chat_id=-448206260, text='123', parse_mode=telegram.ParseMode.HTML))
