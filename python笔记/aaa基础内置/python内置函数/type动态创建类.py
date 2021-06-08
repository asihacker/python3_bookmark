#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 20:56
# @Author  : AsiHacker
# @File    : type动态创建类.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.、
# https://blog.csdn.net/sinat_38682860/article/details/109359544

"""
当type（）只有一个参数时，其作用就是返回变量或对象的类型

当type（）有三个参数时，其作用就是创建类对象：

第一个参数：name表示类名称，字符串类型
第二个参数：bases表示继承对象（父类），元组类型，单元素使用逗号
第三个参数：attr表示属性，这里可以填写类属性、类方式、静态方法，采用字典格式，key为属性名，value为属性值
"""
t = type("hello", (), {"a": 1, "hello": 'asi'})
c = t()
print(c.a)
print(t.a)
