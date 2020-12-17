#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 16:01
# @Author  : AsiHacker
# @File    : 多父类调用顺序.py
# @Software: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 16:08
# @Author  : AsiHacker
# @Site    :
# @File    : demo.py
# @Software: PyCharm
class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")

# 总结 如果上述的解释太过于难以理解，我们可以简单记住，self.method() 将会先在当前类中查看 method() 方法，
# 如果没有，就在继承链中进行查找，查找顺序就是你继承的顺序从左到右，直到 method() 方法被找到。super().method()
# 与 self.method() 是差不多的，只是 super().method() 需要跳过当前类而已。
