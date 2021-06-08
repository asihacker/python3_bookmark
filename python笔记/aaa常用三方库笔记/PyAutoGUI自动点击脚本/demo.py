#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 09:20
# @Author  : AsiHacker
# @File    : asyncio-demo-1.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pyautogui as pag

# mac需要点击安全与隐私=>辅助功能=>pycharm
pag.PAUSE = 1.5  # 暂停1.5秒
pag.click(50, 167)
pag.click(50, 167)
# 点击
# pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0)
# 其中x，y是坐标，clicks 是点击次数，interval 是点击间隔，button 指代三个鼠标按钮的哪一个，duiation 是点击之间的间隔。
# 输入
# 输入 ASCII 字符和键盘击键、热键分别如下：
# 输入 ASCII 字符串是typewrite(message='test message.',interval=0.5)
# 击键是press('esc')
# 按下是KeyDown('ctrl')
# 松开是KeyUp('ctrl')
# 组合键是hotkey('ctrl','v')。
# 汉字输入
# import pyperclip
#
# #以下读入内容，就是把内容存入剪贴板。
# pyperclip.copy('需要输入的汉字')
# #以下输出内容，就是粘贴。
# pag.hotkey('ctrl','v')
