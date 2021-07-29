# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 20:05
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Parent:
    def __init__(self):
        self.name = "MING"
        self.__wife = "Julia"  # _一个表示私有不希望呗调用，__2个表示不希望被子类继承


class Son(Parent):
    def __init__(self):
        self.name = "Xiao MING"
        super().__init__()


a = Son()
pass
