#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 23:30
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pickle

# 有人会问，既然json和pickle的功能是一样的，那么为什么还要存在两个模块呢？
# json支持的数据类型：int,str,tuple,list,dir，可以跨平台
# pickle支持的数据类型：支持python里所有的数据类型 缺点：只能在python中使用
d = {'name': 'alex', 'age': 22}

s = pickle.dumps(d)
print(s)
print(pickle.loads(s))
# 保存到文件
d = {'name': 'alex', 'age': 22}

f = open("test.pkl", "wb")
pickle.dump(d, f)
f.close()
f = open("test.pkl", "rb")
d = pickle.load(f)
print(d)  # {'name呢': 'alex', 'age': 22}
f.close()
