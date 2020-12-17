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
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
row0 = ['编号', '单位', '网站备案号', '域名', u'外链名称', u'不良网站名', u'不良url地址', u'地市', u'ip地址', u'截图', u'备注', u'审核时间', u'父链接',
        u'源码超链接']
row1 = [row0 for _ in range(100)]
# 生成第一行
for h in range(len(row1)):
    for l in range(len(row0)):
        print(h, l)
        sheet1.write(h, l, row0[l])  # 顺序为x行x列写入第x个元素
f.save('newfile.xls')
