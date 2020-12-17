#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 19:45
# @Author  : AsiHacker
# @File    : property的setter getter deleter.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Goods:

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price  # 获取商品价格
obj.price = 200  # 修改商品原价
print(obj.price)
del obj.price  # 删除商品原价
