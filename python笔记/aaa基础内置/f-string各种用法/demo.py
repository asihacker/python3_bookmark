#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 10:18
# @Author  : AsiHacker
# @File    : json模块.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime

a = 10
b = 'Áeiöu'
c = 'abcdefg'


def test_func():
    return 66


class Color:
    def __init__(self, r: float = 255, g: float = 255, b: float = 255):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return "A RGB color"

    def __repr__(self) -> str:
        return f"Color(r={self.r}, g={self.g}, b={self.b})"


d = Color(r=123, g=32, b=255)
print(f'我今年{a}了\n')
print(fr'我今年{a}了\n')
print(f'hahaha {a * a}')
print(f'hahaha {a * a=}')
print(f'hahaha {test_func()}')
print(f'hahaha {test_func()=}')
# 进制转化打印
print(f'{a:b}')  # 格式化为2进制输出
print(f'{a:x}')  # 格式化为16进制输出
print(f'{a:X}')  # 格式化为16进制输出
print(f'{a:d}')  # 格式化为10进制输出
# __str__ 和 __rerp__
print(f'{d}')  # 默认打印__str__
print(f'{d!s}')  # 默认打印__str__
print(f'{d!r}')
print(f'{b!a}')  # 转义ASCII字符

e = 1.223234
print(f'{e:.2f}')
print(f'{e:.2%}')
# 填充长度 >  < 小的一个方向表示字符串对齐的位置 ^表示剧中 *表示用什么填充
f = 'AsiHacker'
print(f'{f:>100}')
print(f'{f:<100}')
print(f'{f:^100}')
print(f'{f:*^100}')
# 转义符号{}
g = 'hello'
print(f'{{g}}={g}')

# 如何使用逗号千分位分隔符数字
f = 123456789.32342
print(f'{f:,.2f}')
print(f'{f:e}')
# 格式化时间
now = datetime.datetime.now()
print(f'{now}')
print(f'{now:%Y-%m-%d %H:%M:%S}')
# 如何在字符串前补零
g = 42
# 可以用{expr:0len} 这个方法来进行字符串补零。len是最终返回字符串的长度。还可以增加一个正负号标记。在这种情况下，用+则无论数值为正负数都将显示相应正负号。用-则只有当数值为负数时才显示负号，默认设定也是如此。
print(f'{g:05}')
