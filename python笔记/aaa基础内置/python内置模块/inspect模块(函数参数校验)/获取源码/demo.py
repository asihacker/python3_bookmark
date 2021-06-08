#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 20:40
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
"""
1. inspect.getdoc(object)： 获取object的documentation信息

2. inspect.getcomments(object)

3. inspect.getfile(object): 返回对象的文件名

4. inspect.getmodule(object)：返回object所属的模块名

5. inspect.getsourcefile(object)： 返回object的python源文件名；object不能使built-in的module, class, mothod

6. inspect.getsourcelines(object)：返回object的python源文件代码的内容，行号+代码行

7. inspect.getsource(object)：以string形式返回object的源代码

8. inspect.cleandoc(doc)：
"""
import inspect
import os

print(inspect.getdoc(os))  # 获取文档
print(inspect.getsource(os))  # 获取源码
