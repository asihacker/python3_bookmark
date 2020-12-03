#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 20:00
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [1, 2, 3, 4, 5, 9])

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
