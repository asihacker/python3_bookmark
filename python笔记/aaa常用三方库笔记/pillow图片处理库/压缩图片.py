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
# https://blog.csdn.net/Together_CZ/article/details/107974509?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_v2~rank_aggregation-2-107974509.pc_agg_rank_aggregation&utm_term=%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AD%97%E8%8A%82%E6%B5%81&spm=1000.2123.3001.4430
if __name__ == '__main__':
    rsp = requests.get(
        "https://ap-guangzhou-1257892306.cos.ap-guangzhou.myqcloud.com/image/Adidas%20Yeezy%20350%20v2%20Non-refelective%20white%201.jpg")

    image = Image.open(BytesIO(rsp.content))
    print("初始尺寸", image.size)
    image.save('test222.jpg')
    image.thumbnail((image.height * 0.2, image.width * 0.2))
    print("默认缩放NEARESET", image.size)
    image.save('test2.jpg')
    # image.save('test80.jpg', quality=80)
    # image.save('test10.jpg', quality=10)
    # 将Image对象转成bytes或者BytesIO
    image.getvalue()
