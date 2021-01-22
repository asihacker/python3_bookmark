#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 18:48
# @Author  : AsiHacker
# @File    : 代理.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
capabilities = DesiredCapabilities.CHROME
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
# chrome_options.add_argument('--headless')  # 增加无界面选项
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.add_argument('--proxy-server=socks5://8.134.35.218:8090')  # 设置代理
chrome_options.add_argument('--proxy-server=http://8.134.35.218:8090')  # 设置代理
chrome_options.add_argument(
    f'user-agent={ua}')
browser = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
browser.get("https://httpbin.org/get")
time.sleep(5)
browser.get("http://www.okooo.com/soccer/match/1123586/odds/")

