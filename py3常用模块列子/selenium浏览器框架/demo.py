#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 19:18
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
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
# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(options=chrome_options)
mainUrl = "https://www.facebook.com/"
browser.get(mainUrl)
# print(f"browser text = {browser.page_source}")
cookies = [{"domain": "facebook.com", "expiry": 1619924175, "httpOnly": True, "name": "xs", "path": "/", "secure": True,
            "value": "193%3ALB3RUFtDfhSMLQ%3A2%3A1588388184%3A8347%3A3538"},
           {"domain": "facebook.com", "expiry": 1619924175, "httpOnly": False, "name": "c_user", "path": "/",
            "secure": True, "value": "100004040823246"},
           {"domain": "facebook.com", "expiry": 1651460142, "httpOnly": True, "name": "datr", "path": "/",
            "secure": True, "value": "IOGsXprd8xxfYAuu6AW7ZmoL"},
           {"domain": "facebook.com", "expiry": 1596164204, "httpOnly": True, "name": "fr", "path": "/", "secure": True,
            "value": "1uKwm1LFev1sTKPOF.AWVgMi1UUBD1SRc7NqqRFCX1U30.BerOEg.4E.F6s.0.0.BerOF0.AWX0hwkg"},
           {"domain": "facebook.com", "expiry": 1651460177, "httpOnly": True, "name": "sb", "path": "/", "secure": True,
            "value": "IOGsXvx3Qx0Yn-1LmZd5cdoI"}]
for cookie in cookies:
    browser.add_cookie(cookie)
# browser.find_element_by_xpath('//*[@id="email"]').send_keys('100053725548951')
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="pass"]').send_keys('m4o993PeMr')
# time.sleep(1)
# # browser.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').send_keys('ykt007')
# # time.sleep(1)
# browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
# time.sleep(10)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div').click()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/div/input').send_keys(
#     '008615990767710')
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[6]/div/button[1]').click()
# time.sleep(1)
print(browser.get_cookies())
# browser.quit()
