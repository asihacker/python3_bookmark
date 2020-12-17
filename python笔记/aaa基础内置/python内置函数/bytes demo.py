#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 22:08
# @Author  : AsiHacker
# @Site    : 
# @File    : bytes 自定义异常.py
# @Software: PyCharm
print(bytes('中国', encoding='utf-8'))
print(bytes('中国', encoding='UTF-8'))  # 编码格式不区分大写小写
print(bytes('中国', encoding='gbk').hex())
