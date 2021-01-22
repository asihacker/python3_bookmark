#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 14:13
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pysnooper

out = list()


@pysnooper.snoop()  # output='debug.log'
def demo_func():
    """

    :return:
    """
    global out
    profile = dict()
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"
    out.append(100)
    return profile


# prefix 前缀 可以在输出信息前面加上前缀，方便识别。
# watch 用来监控外部变量 @pysnooper.snoop(watch=('out["foo"]', 'foo.bar', 'self.foo["bar"]'))
# watch_explode 用来监控外部变量 但是和上面的相反 @pysnooper.snoop(watch_explode=('foo', 'bar')) 表示除了 foo 和 bar 其他都监听。
# depth 跟踪深度 比如方法里面调用方法里面再调用方法 要跟踪里面的话就设置这个参数
# output 输出日志到文件 @pysnooper.snoop(output="/var/log/debug.log")
# max_variable_length 设置最大输出长度 默认最大输出长度为100，也就是超过100的会被截断 通过这个可以设置最大长度。max_variable_length=None它从不截断它们
# thread_info 打印线程id

if __name__ == '__main__':
    demo_func()
