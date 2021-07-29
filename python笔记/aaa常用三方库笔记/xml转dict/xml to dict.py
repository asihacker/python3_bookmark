# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 10:49
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# coding:utf-8
import xmltodict  # 导入

# XML格式字符串
xml_str = """
        <xml>
            <Name>张三</Name>
            <age>18</age>
        </xml>
        """

xml_dict = xmltodict.parse(xml_str)  # 解析xml字符串

print(type(xml_dict))  # <class 'collections.OrderedDict'>  类字典型，可以按照字典方法操作

print(xml_dict)

# 遍历
for key, val in xml_dict['xml'].items():
    print(key, "---", val)
