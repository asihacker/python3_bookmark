#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 15:37
# @Author  : AsiHacker
# @File    : 继承多类.py
# @Software: PyCharm
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self, *args, **kwargs):
        print('普通员工在写代码，工资为：', self.salary)


class Customer:
    def __init__(self, favourite, address):
        self.favourite = favourite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是：%s,地址是%s' % (self.favourite, self.address))


class Mannager(Employee, Customer):
    def __init__(self, salary, favourite, address):
        print('Manngaer的构造方法')
        # 方法一：用未绑定方法来构造,使用类名直接构造,逐个调用
        # Employee.__init__(self,salary)
        # Customer.__init__(self,favourite,address)

        # 方法二：使用super()和未绑定方法
        super().__init__(salary)
        # 与上一行代码效果相同
        # super(Mannager,self).__init__(salary)
        Customer.__init__(self, favourite, address)


m = Mannager(25000, 'it产品', '广州')
m.work()
m.info()
