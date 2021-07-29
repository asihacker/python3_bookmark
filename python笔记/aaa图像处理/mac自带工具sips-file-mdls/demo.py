#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 14:40
# @Author  : AsiHacker
# @File    : demo.txt.txt-svg.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
###命令行转化图片格式
"""
sips可以转换一个或多个图片文件的文件格式
sips -s format [格式名称] [文件名] --out [输出文件的名称]

sips -s format png goswift.jpg --out goswift.png

要想批量转换图片文件，我们需要使用下面命令格式
for i in [文件名]; do sips -s format [格式名称] $i --out [终点]/$i.[格式名称];done

for i in *.jpeg; do sips -s format png $i --out Doc/$i.png;done
"""
###按比例缩放

"""
sips -Z 600 goswift.png
sips -z 300 600 goswift.png
"""

###查看图片信息

"""
file go-swift.png //文件信息
mdls go-swift.png //可以获取到图片详细信息
"""
