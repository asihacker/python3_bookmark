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
