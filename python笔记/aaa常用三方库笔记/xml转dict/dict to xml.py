# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 10:50
# @Author  : AsiHacker
# @File    : dict to xml
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# coding:utf-8
import xmltodict  # 导入

# 字典
xml_dict = {
    "xml": {
        "name": u"张三",
        "age": 18
    }
}

# 字典转换成XML字符串
# xml_str = xmltodict.unparse(xml_dict)
xml_str = xmltodict.unparse(xml_dict, pretty=True)  # pretty表示友好输出（有换行）

print(xml_str)
