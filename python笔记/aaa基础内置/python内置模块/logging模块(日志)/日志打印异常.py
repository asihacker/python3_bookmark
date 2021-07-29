#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 12:22
# @Author  : AsiHacker
# @File    : 日志打印异常.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
try:
    open("sklearn.txt", "rb")
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    # logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)
    logger.exception('Faild to open sklearn.txt from logger.error')

logger.info("Finish")
