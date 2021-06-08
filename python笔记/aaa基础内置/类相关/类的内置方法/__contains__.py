#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:41
# @Author  : AsiHacker
# @File    : __contains__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 在Class里添加__contains__(self,x)函数,可判断我们输入的数据是否在Class里.参数x就是我们传入的数据.
class Graph():
    def __init__(self):
        self.items = {'a': 1, 'b': 2, 'c': 3}

    def __contains__(self, x):  # 判断一个定点是否包含在里面
        return x in self.items


a = Graph()
print('a' in a)  # 返回True
print('d' in a)  # 返回False
