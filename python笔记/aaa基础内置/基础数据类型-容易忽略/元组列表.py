#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 22:22
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm


# 元组
a = (1,)
b = (1, 2, 4, 5, 3)
# 元组只可以看 不能增加删除修改 但是可以连接

print(a + b)

c = [1, 2, 3]
d = [3, 4, 5, 6]
print(c + d)
c.extend(d)  # 批量添加多个成员，放可迭代对象（list也是可迭代对象）
print(c)
