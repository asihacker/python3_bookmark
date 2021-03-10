#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:33
# @Author  : AsiHacker
# @File    : 上下文管理__enter__() 与 __exit__().py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 使用 with as 会执行enter与exit
#
# __exit__() 的执行代表了整个 with 语句的执行完毕
#
# 用途或者说好处：
#
# 1.使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
#
# 2.在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处
class Test:
    def __init__(self, name):
        self.name = name

    def __enter__(self):  # 使用 with 关键字时会执行。返回一个对象赋值给 as 后的对象。
        print('执行了enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 所有代码块内的过程运行完毕或者发生异常时候执行
        print('执行了exit')

        # 当没有异常信息时候 exc_type, exc_val, exc_tb 都为 None
        # 有异常信息时候会抛出异常。
        print(exc_type)  # <class 'NameError'> 异常类
        print(exc_val)  # name 'asdfasdfasdfagdasgerghae' is not defined    异常原因
        print(exc_tb)  # <traceback object at 0x000000000111C848>  异常的追踪信息

        # 如果在__exit__()中返回一个 True ，with,as 代码块中的异常将结束代码块，继续执行代码块外的程序 并不会抛出异常。
        return True


print('=' * 50)
with Test('bet.txt') as f:  # ----> f = Test.__enter__() 使用with关键字会执行__enter__()函数，然后由__enter__()返回一个对象赋值给f
    print(f)
    print(f.name)
    print(asdfasdfasdfagdasgerghae)
    print('当__exit__()return True时候会跳过异常后的语句直接执行代码块外的语句')

print('=' * 50)
