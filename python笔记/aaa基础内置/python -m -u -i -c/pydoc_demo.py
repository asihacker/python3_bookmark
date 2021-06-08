#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:58
# @Author  : AsiHacker
# @File    : pydoc_demo.py
# @Software: PyCharm

# python -m pydoc -w xxx.py #查看指定py文件 或者 库的在线文档 会生产html在本地
# python -m pydoc -p 1314 #打开一个web端口来查看

# Python文档工具
#
# pydoc <名称>…
# 显示某些东西的文本文档。<name>可能是a的名称
# Python关键字、主题、函数、模块或包，或点号
# 对模块内或模块中的类或函数的引用
# 包中。如果<name>包含一个'/'，它将被用作到a的路径
# Python源文件到文档。如果名称为“关键词”、“主题”，
# 或'modules'，就会显示这些东西的列表。
#
# pydoc - k <关键字>
# 在所有可用模块的概要行中搜索关键字。
#
# pydoc - n <主机名>
# 使用给定的主机名(默认为localhost)启动HTTP服务器。
#
# pydoc - p <端口>
# 在本地机器上的给定端口上启动HTTP服务器。港口
# 数字0可用于获取任意未使用的端口。
#
# pydoc - b
# 在任意未使用的端口上启动HTTP服务器并打开Web浏览器
# 交互式浏览文档。此选项可用于
# -n和/或-p的组合。
#
# pydoc -w <name>…
# 将模块的HTML文档写到当前文件中
# 目录中。如果<name>包含一个'/'，它将被视为一个文件名;如果
# 它命名一个目录，为所有的内容编写文档。
