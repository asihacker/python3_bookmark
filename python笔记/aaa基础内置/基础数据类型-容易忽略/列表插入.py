#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:38
# @Author  : AsiHacker
# @Site    : 
# @File    : 列表插入.py
# @Software: PyCharm
# insert()函数：将新元素添加到指定索引号前面
#
# 再来一个元素'0'，它比'1'要小，想让它添加到列表的最前面。可以用insert()函数实现：
#
# insert(index, object)
#
# 它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素

a = [1, 2, 3, 4, 5]
a.insert(0, 0)
a.append(1)
a.append(1)
a.append(1)
a.append(1)
print(a)
