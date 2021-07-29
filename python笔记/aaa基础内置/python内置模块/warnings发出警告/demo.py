#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 11:55
# @Author  : AsiHacker
# @File    : md5-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# import warnings

# warnings.warn('This is a warning message')
# 如果不想看到警告可以 python -W ignore Process启动子进程.py !!!!!
import warnings

# warnings.filterwarnings("ignore")  # 这样可以忽略警告
warnings.filterwarnings(action='error')  # 这里指定针对异常的处理态度，这里指定为error则可以被try捕捉

"""
Warning	所有警告类别类的基类，它是 Exception 的子类
UserWarning	函数 warn() 的默认类别
DeprecationWarning	用于已弃用功能的警告（默认被忽略）
SyntaxWarning	用于可疑语法的警告
RuntimeWarning	用于有关可疑运行时功能的警告
FutureWarning	对于未来特性更改的警告
PendingDeprecationWarning	对于未来会被弃用的功能的警告（默认将被忽略）
ImportWarning	导入模块过程中触发的警告（默认被忽略）
UnicodeWarning	与 Unicode 相关的警告
BytesWarning	与 bytes 和 bytearray 相关的警告 (Python3)
ResourceWarning	与资源使用相关的警告(Python3)
"""


class Apple:
    def test(self):
        warnings.warn("use driver.switch_to.frame instead", DeprecationWarning)


c = Apple()

try:
    c.test()
except Warning as w:
    print(w)
    pass
