#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 17:25
# @Author  : AsiHacker
# @File    : __init__.py.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# a)uuid.uuid1([node[, clock_seq]]): 基于时间戳
# 
# 　　使用主机ID, 序列号, 和当前时间来生成UUID, 可保证全球范围的唯一性.但由于使用该方法生成的UUID中包含有主机的网络地址, 因此可能危及隐私.该函数有两个参数, 如果node参数未指定, 系统将会自动调用getnode()函数来获取主机的硬件地址.如果clock_seq参数未指定系统会使用一个随机产生的14位序列号来代替.
# 
# b)uuid.uuid3(namespace, name): 基于名字的MD5散列值
# 
# 　　通过计算命名空间和名字的MD5散列值来生成UUID, 可以保证同一命名空间中不同名字的唯一性和不同命名空间的唯一性, 但同一命名空间的同一名字生成的UUID相同.
# 
# c) uuid.uuid4(): 基于随机数
# 
# 　　通过随机数来生成UUID.使用的是伪随机数有一定的重复概率.
# 
# d)uuid.uuid5(namespace, name): 基于名字的SHA - 1
# 散列值
# 
# 　　通过计算命名空间和名字的SHA - 1
# 散列值来生成UUID, 算法与uuid.uuid3()相同.
import uuid

print(uuid.uuid1())
print(uuid.uuid4())
