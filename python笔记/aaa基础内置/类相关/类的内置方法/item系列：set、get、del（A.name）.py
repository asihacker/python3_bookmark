#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:13
# @Author  : AsiHacker
# @File    : item系列：set、get、del（A.name）.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 好文章=>  https://www.cnblogs.com/zbuter/p/8746004.html
class Test:

    def __setattr__(self, key, value):
        print('__setattr__')
        self.__dict__[key] = value

    def __getattr__(self, item):
        """
        getattr 方法
        使用对象取值、赋值或者删除时，会默认的调用对应的__getattr__、__setattr__、__delattr__方法。
        对象取值时，取值的顺序为：先从object里__getattribute__中找，第二步从对象的属性中找，第三步从当前类中找，
        第四步从父类中找，第五步从__getattr__中找，如果没有，直接抛出异常。
        :param item:
        :return:
        """
        print('__getattr__')
        return self.__dict__[item]

    def __delattr__(self, key):
        print('__delattr__')
        self.__dict__.pop(key)

    def __setitem__(self, key, value):
        print('__setitem__')
        self.__dict__[key] = value

    def __getitem__(self, item):
        print('__getitem__')
        return self.__dict__[item]

    def __delitem__(self, key):
        print('__delitem__')
        self.__dict__.pop(key)

    def test(self):
        print('func')

    def __getattribute__(self, attr):
        print("开始属性校验拦截功能")
        print(attr)
        return object.__getattribute__(self, attr)


f = Test()
f.test()
f.a = 123  # 使用 . 的方式不会调用 __setitem__() 方法,使用__setattr__方法
f['bet'] = 123  # 使用 [] 的方式才会调用 __setitem__() 方法

print(f.a)  # 使用 . 的方式不会调用 __getitem__() 方法
print(f['bet'])  # 使用 [] 的方式才会调用 __getitem__() 方法

# del f.bet       # 使用 . 的方式不会调用 __delitem__() 方法
del f['bet']  # 使用 [] 的方式才会调用 __delitem__() 方法
delattr(f, 'bet')
# 使用 . 的方式 与 attr 系列方法有关。  使用 [] 的方式与 item 系列方法有关
f.test()
