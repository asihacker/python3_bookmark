#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 14:01
# @Author  : AsiHacker
# @File    : 给函数设置超时机制.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from moviepy.editor import *

video = VideoFileClip('123.flv')  # 视频所在路径
audio = video.audio.subclip(t_start=18, t_end=None)  # 表示18秒开始
audio.write_audiofile('bgm.wav')  # 音频所在路径
