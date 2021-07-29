#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 12:44
# @Author  : AsiHacker
# @File    : loggin-rich.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import logging

from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

log = logging.getLogger("rich")
log.info("Hello, World!",extra={"markup": True})
