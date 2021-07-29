# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 22:22
# @Author  : AsiHacker
# @File    : demo.txt.txt
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 小数据池
# 小数据池，也称为小整数缓存机制，或者称为驻留机制等
#
# 大前提：小数据池也是只针对 int(float)，str，bool。
#
# 小数据池是针对不同代码块之间的缓存机制！！！

# 小数据池包括 int(float)，str，bool。
# https://www.cnblogs.com/hnlmy/p/10634606.html#autoid-0-0-0

# Python 对小整数的定义是 [-5, 256] 这些整数对象是提前建立好的，不会被垃圾回收
# intern机制处理空格一个单词的复用机会大，所以创建一次，有空格创建多次，但是字符串长度大于20，就不是创建一次了。
# 大整数池
# https://www.cnblogs.com/fmgao-technology/p/9261794.html?ivk_sa=1024320u
a = 256
b = 256
print(id(a) == id(b))
a = 257
b = 257
print(id(a) == id(b))
