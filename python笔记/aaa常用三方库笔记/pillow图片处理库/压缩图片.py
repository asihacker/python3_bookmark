#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 18:11
# @Author  : AsiHacker
# @File    : 压缩图片.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import requests
from io import StringIO, BytesIO
from PIL import Image

# 教程地址
# https://tefuirnever.blog.csdn.net/article/details/90597048?utm_medium=distribute.pc_relevant.none-task-blog-OPENSEARCH-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-OPENSEARCH-2.control
if __name__ == '__main__':
    rsp = requests.get(
        "https://nanshan-1257892306.cos.ap-guangzhou.myqcloud.com/photo/19d40132c4e1e0aee62ed2fc80c70dc8.jpg")

    image = Image.open(BytesIO(rsp.content))
    print("初始尺寸", image.size)
    image.save('test1.jpg')
    image.thumbnail((image.height * 0.7, image.width * 0.7))
    print("默认缩放NEARESET", image.size)
    image.save('test2.jpg')
    # image.save('test80.jpg', quality=80)
    # image.save('test10.jpg', quality=10)
    # 将Image对象转成bytes或者BytesIO
