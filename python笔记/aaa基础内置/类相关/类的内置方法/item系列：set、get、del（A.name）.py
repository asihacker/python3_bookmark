#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:13
# @Author  : AsiHacker
# @File    : item系列：set、get、del（A.name）.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Test:

    def __setitem__(self, key, value):
        print('setitem')
        self.__dict__[key] = value

    def __getitem__(self, item):
        print('getitem')
        return self.__dict__[item]

    def __delitem__(self, key):
        print('del')
        self.__dict__.pop(key)


f = Test()

f.a = 123  # 使用 . 的方式不会调用 __setitem__() 方法
f['a'] = 123  # 使用 [] 的方式才会调用 __setitem__() 方法

print(f.a)  # 使用 . 的方式不会调用 __getitem__() 方法
print(f['a'])  # 使用 [] 的方式才会调用 __getitem__() 方法

# del f.a       # 使用 . 的方式不会调用 __delitem__() 方法
del f['a']  # 使用 [] 的方式才会调用 __delitem__() 方法

# 使用 . 的方式 与 attr 系列方法有关。  使用 [] 的方式与 item 系列方法有关
