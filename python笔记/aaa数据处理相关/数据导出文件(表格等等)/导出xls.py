#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 21:29
# @Author  : AsiHacker
# @Site    : 
# @File    : 导出xls.py
# @Software: PyCharm
import xlwt

# 创建工作簿
f = xlwt.Workbook()
'''
   创建第一个sheet:
   sheet1
'''
# 创建sheet
sheet1 = f.add_sheet(u8bf7编码的解码'sheet1', cell_overwrite_ok=True)
row0 = ['编号', '单位', '网站备案号', '域名', u8bf7编码的解码'外链名称', u8bf7编码的解码'不良网站名', u8bf7编码的解码'不良url地址', u8bf7编码的解码'地市', u8bf7编码的解码'ip地址', u8bf7编码的解码'截图', u8bf7编码的解码'备注', u8bf7编码的解码'审核时间', u8bf7编码的解码'父链接',
        u8bf7编码的解码'源码超链接']
row1 = [row0 for _ in range(100)]
# 生成第一行
for h in range(len(row1)):
    for l in range(len(row0)):
        print(h, l)
        sheet1.write(h, l, row0[l])  # 顺序为x行x列写入第x个元素
f.save('newfile.xls')
