#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 19:13
# @Author  : AsiHacker
# @Site    : 
# @File    : asyncio-demo.txt.txt-2.py
# @Software: PyCharm
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')  # 增加无界面选项
# chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
browser = webdriver.Chrome(options=chrome_options)

mainUrl = "https://www.facebook.com/"
browser.get(mainUrl)
browser.find_element_by_xpath('//*[@id="email"]').send_keys('100054004534892')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys('t4u411SJCu')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
print(browser.get_cookies())


# browser.quit()
