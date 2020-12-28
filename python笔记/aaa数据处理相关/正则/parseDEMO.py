#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 09:15
# @Author  : AsiHacker
# @Site    : 
# @File    : parseDEMO.py
# @Software: PyCharm
from parse import *

aaa = 'mark我叫小明，我今年25岁了，我最喜欢 篮球 足球 乒乓球 羽毛球。谢谢大家      2020-09-07 12:31:23     '
result = parse('{hah}我叫{name}，我今年{age:d}岁了，我最喜欢 {foo} {foo2} {foo3} {foo4}。谢谢大家{time:>}', aaa,
               case_sensitive=False)
print(result)
# {age:d} :d 表示转化为整数
# {age:^} :^ 表示去除两边空格
# {age:>} :^ 表示去除左边空格
# {age:<} :^ 表示去除右边空格 （指哪边，哪边不去除）
# case_sensitive：敏感开关 True表示开启大小写 False表示不开启大小写
# 重复利用 pattern
from parse import compile

# 就是说一个匹配规则可以用生成一个解析对象，然后给别的地方用
pattern = compile("I am {}, {} years old, {}")
result = pattern.parse("I am Jack, 27 years old, male")
print(result)
