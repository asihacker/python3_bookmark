#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 12:32
# @Author  : AsiHacker
# @File    : 抽象demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from abc import *


class Fruit(ABC):

    @abstractmethod
    def color(self):
        ...

    @classmethod
    @abstractmethod
    def eat(cls):
        ...

    @staticmethod
    @abstractmethod
    def look(self):
        ...


class Apple(Fruit):


    def test(self):
        print(123)

    def color(self):
        print('red')

    @classmethod
    def eat(cls):
        print('eat')

    @staticmethod
    def look():
        print('look')


if __name__ == '__main__':
    a = Apple()
    a.test()
    a.eat()
    Apple.look()
