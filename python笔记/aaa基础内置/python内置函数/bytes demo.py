#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 22:08
# @Author  : AsiHacker
# @Site    : 
# @File    : bytes 自定义异常.py
# @Software: PyCharm
print(bytes('中国', encoding='utf-8'))
print(bytes('中国', encoding='UTF-8'))  # 编码格式不区分大写小写
print(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(bytes('中国', encoding='gbk').hex())
# 字符串是字符组成的有序序列，字符可以使用编码来理解：
# bytes 是字节组成的有序的不可变序列；
# bytearry 是字节组成的有序的可变序列；
