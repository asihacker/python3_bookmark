#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 16:16
# @Author  : AsiHacker
# @File    : demo3.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pyecharts.options as opts
from pyecharts.charts import Line

x = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期七', '星期日']
y1 = [100, 200, 300, 400, 100, 400, 300]
y2 = [200, 300, 200, 100, 200, 300, 400]
line = (
    Line()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="y1线", y_axis=y1, is_smooth=True)
        .add_yaxis(series_name="y2线", y_axis=y2, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-多折线重叠"))
)
line.render('line_chart.html')
