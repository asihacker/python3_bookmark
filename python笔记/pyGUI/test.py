#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 15:04
# @Author  : AsiHacker
# @Site    : 
# @File    : 重复元素判定.py
# @Software: PyCharm

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('1.png'))
        qle = QLineEdit(self)
        qle.move(10, 10)
        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
