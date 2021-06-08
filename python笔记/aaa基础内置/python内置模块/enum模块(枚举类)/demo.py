#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 15:26
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from enum import Enum, unique



# 使用枚举类有哪些好处
# 枚举类可以方便地表示星期，月份等常数类型，如果你不用枚举类，那么你只能用数字或者字符串。
# 如果你使用数字，用1-7来表示星期数，但一个数字在程序中不仅可以表示星期数，可能还有其他许多含义，
# 这样你在写程序时就必须时刻记住这些数字的含义，这降低了程序的可读性，也导致容易出错。而当你使用字符串时，
# 虽然没有明显的缺点，但在内存中字符串所占内存要比数字多，这就降低了程序的效率。
#
# 枚举类正好弥补了这两方面的缺点，你可以在代码中使用枚举类，但在内存中存放时使用的是数字，
# 既提高了可读性，又提高了程序效率。更重要的是，Python中的枚举类型是不可变类型，又可以进行迭代，
# 这就意味着你可以随时使用枚举类型而不用担心改变了枚举类型的值。
@unique  # 枚举类型默认可以对相同的值使用别名，但有时我们需要确保枚举类型不能重复，我们也有办法使每个枚举值只出现一次。我们可以引入装饰器“@unique”
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7


class ColorE():
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7


Color2 = Enum("Color", ('red', 'green', 'blue'))
Color3 = ColorE()

for k in Color:
    print(k, k.name, k.value)

print(Color.red)
print(Color['red'])
# print(Color(60))
Color.red = 10  # 枚举类无法改变值


# 比如在facebook协议中使用枚举类来定义固定参数标记
class PostParam(Enum):
    EVERYONE = 300645083384735
    NETWORKS_FRIENDS = 123780391104836
    FRIENDS_OF_FRIENDS = 275425949243301
    FRIENDS = 291667064279714
    FRIENDS_MINUS_ACQUAINTANCES = 284920934947802
    ONLY_ME = 286958161406148
    FB_ONLY = 411331705596297
    EVENT_PUBLIC = 1493271774218406
    EVENT_INVITE_ONLY = 599950423437029
