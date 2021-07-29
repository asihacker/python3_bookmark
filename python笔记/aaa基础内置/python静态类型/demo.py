#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 17:00
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 参数name的类型是未知的
# 返回的类型也是未知的
# https://www.cnblogs.com/neozheng/p/14096030.html
from typing import Iterable, Union, Optional

a = ...
print(a)


def greeting(name):
    return 'Hello ' + name


# 参数name后面跟了:str 代表name期望是str类型
# 参数括号后面跟了->str代表返回类型为str类型
def greeting2(name: str) -> str:
    return 'Hello ' + name


x: str = 'xxx'  # 声明一个变量为str类型
greeting2(x)  # Hello xxx


# greeting2(123)  # TypeError: can only concatenate str (not "int") to str


# 参数names为list类型并且元素都是str类型
# 返回为None
def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)  # Ok!


# greet_all(ages)  # 出错了 Error due to incompatible types


# Dict[int, str] int代表key类型， str代表val类型
# def debug(t: dict[int, str]) -> dict:
#     return t
#
#
# debug({1: '234'})  # {1: '234'}


# def greeting3(names: Iterable[str]) -> None:
#     for name in names:
#         print(name)
#
#
# greeting3(['aaa', 'bbb'])  # list aaa bbb
# greeting3(('ccc', 'ddd'))  # tuple ccc ddd
# greeting3({'eee', 'fff'})  # set eee fff
# greeting3({'ggg': 'hhh'})  # dict ggg
# greeting3('123')  # str 1 2 3
# greeting3(678)  # error: Argument 1 to "greeting" has incompatible type "int"; expected "Iterable[str]"


# Union
# 接受多个指定类型，但不接受除此外的类型
def test1(a: Union[str, int, None]):
    print(type(a), a)


test1(1)
test1('1')
test1(1.00210923)
test1(None)
test1(None)


def test2(a: Optional[float]):  # Optional[X] == Union[X, None].
    print(type(a), a)


#
test2(None)
test2(1)
test2('1')
test2(1.00210923)


def test3(a: Union[int, str, float]):
    print(type(a), a)


test3(1)
test3('1')
test3(1.00210923)


def test4(a: Union[list[str], dict[str, int]]):
    print(1)


test4(a=['2'])
test4(a=[1])
test4(a={'a': 1})
test4(a={'a': '1'})
