#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 21:14
# @Author  : AsiHacker
# @File    : currentframe-栈与帧.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import inspect
import pprint


def recurse(limit, keyword="default", *, kwonly="must be named"):
    local_variable = "." * limit
    keyword = "change value of argument"
    frame = inspect.currentframe()
    print("line {} of {}".format(frame.f_lineno, frame.f_code.co_filename))
    pprint.pprint(frame.f_locals)

    print("\n")
    if limit <= 0:
        return
    recurse(limit - 1)
    return local_variable


if __name__ == '__main__':
    recurse(2)
"""
f_back	前一个堆栈帧（朝向调用者），如果这是底部堆栈帧则为None
f_code	在这个框架中执行的Code对象
f_locals	用于查找局部变量的字典
f_globals	用于全局变量
f_builtins	用于内置名称
f_restricted	表示该函数是否在限制执行模式下执行的标志
f_lasti	给出精确的指令（这是代码对象的字节码字符串的索引）
特殊可写属性
f_trace	
f_exc_type	
f_exc_value	
f_exc_traceback	
f_lineno	当前代码在文件中的哪一行
————————————————
版权声明：本文为CSDN博主「NeverLate_gogogo」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/neverlate_gogogo/article/details/107752428
"""