#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:53
# @Author  : AsiHacker
# @File    : 总结-重载运算符.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# __new__	创建类，在 __init__ 之前创建对象
# __init__	类的构造函数，其功能是创建类对象时做初始化工作。
# __del__ 	析构函数，其功能是销毁对象时进行回收资源的操作
# __add__	加法运算符 +，当类对象 X 做例如 X+Y 或者 X+=Y 等操作，内部会调用此方法。但如果类中对 __iadd__ 方法进行了重载，则类对象 X 在做 X+=Y 类似操作时，会优先选择调用 __iadd__ 方法。
# __radd__	当类对象 X 做类似 Y+X 的运算时，会调用此方法。
# __iadd__	重载 += 运算符，也就是说，当类对象 X 做类似 X+=Y 的操作时，会调用此方法。
# __or__	“或”运算符 |，如果没有重载 __ior__，则在类似 X|Y、X|=Y 这样的语句中，“或”符号生效
# __repr__，__str__	格式转换方法，分别对应函数 repr(X)、str(X)
# __call__	函数调用，类似于 X(*args, **kwargs) 语句
# __getattr__	点号运算，用来获取类属性
# __setattr__	属性赋值语句，类似于 X.any=value
# __delattr__	删除属性，类似于 del X.any
# __getattribute__	获取属性，类似于 X.any
# __getitem__	索引运算，类似于 X[key]，X[i:j]
# __setitem__	索引赋值语句，类似于 X[key], X[i:j]=sequence
# __delitem__ 	索引和分片删除
# __get__, __set__, __delete__	描述符属性，类似于 X.attr，X.attr=value，del X.attr
# __len__ 	计算长度，类似于 len(X)
# __lt__，__gt__，__le__，__ge__，__eq__，__ne__ 	比较，分别对应于 <、>、<=、>=、=、!= 运算符。
# __iter__，__next__	迭代环境下，生成迭代器与取下一条，类似于 I=iter(X) 和 next()
# __contains__	成员关系测试，类似于 item in X
# __index__ 	整数值，类似于 hex(X)，bin(X)，oct(X)
# __enter__，__exit__	在对类对象执行类似 with obj as var 的操作之前，会先调用 __enter__ 方法，其结果会传给 var；在最终结束该操作之前，会调用 __exit__ 方法（常用于做一些清理、扫尾的工作）
