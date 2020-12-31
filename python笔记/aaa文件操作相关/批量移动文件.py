#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:16
# @Author  : AsiHacker
# @File    : 批量移动文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from pathlib import Path

target_folder = Path("7788")
target_folder.mkdir(parents=True, exist_ok=True)
source_folder = Path('.')
txt_files = source_folder.glob('*.py')
for txt_file in txt_files:
    filename = txt_file.name
    target_path = target_folder.joinpath(filename)
    print(f"** 移动文件 {filename}")
    print("目标文件存在:", target_path.exists())
    txt_file.rename(target_path)
    print("目标文件存在:", target_path.exists(), '\n')
