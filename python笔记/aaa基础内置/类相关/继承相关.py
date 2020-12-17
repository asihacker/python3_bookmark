#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 11:37
# @Author  : AsiHacker
# @Site    : 
# @File    : 继承相关.py
# @Software: PyCharm
class Apple(object):
    def __init__(self):
        self.name = '小青'
        self.age = 1


class MG(Apple):
    def __init__(self):
        # super().__init__()  # 需要先初始化继承的类 理解，要记得初始化父类，只有初始化了，父类才会相关赋值
        super(MG, self).__init__()
        print(self.age, self.name)


aa = MG()

# 总结 如果上述的解释太过于难以理解，我们可以简单记住，self.method() 将会先在当前类中查看 method() 方法，
# 如果没有，就在继承链中进行查找，查找顺序就是你继承的顺序从左到右，直到 method() 方法被找到。super().method()
# 与 self.method() 是差不多的，只是 super().method() 需要跳过当前类而已。