#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 15:16
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import shortuuid

# pip install shortuuid
# 命令行使用 python3 -m shortuuid
print(shortuuid.uuid())
print(shortuuid.ShortUUID().random(length=10))  # 限制长度
print(shortuuid.get_alphabet())  # 查看随机列表
shortuuid.set_alphabet("asihacker")  # 设置随机列表
print(shortuuid.get_alphabet())  # 将自动排序并从您的字母表中删除重复项以确保一致性
print(shortuuid.uuid())  # 限制长度
