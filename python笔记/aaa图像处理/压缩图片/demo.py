#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 15:26
# @Author  : AsiHacker
# @File    : demo.txt.txt-svg.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import uuid
from io import BytesIO
from PIL import Image
import requests
rsp = requests.get('https://ap-guangzhou-1257892306.cos.ap-guangzhou.myqcloud.com/chatImg/MC40MDA0NjMwMCAxNTk3MjE2Njc3NTA3NjQ3OA%3D%3D.jpeg')

image = Image.open(BytesIO(rsp.content))
image.thumbnail((image.height * 0.8, image.width * 0.8))
tttt = str(uuid.uuid1()) + '.jpg'
image.save(tttt)