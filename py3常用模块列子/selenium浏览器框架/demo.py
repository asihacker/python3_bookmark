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
cookies = [
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'c_user',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': '100053687984351', 'id': 0},
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'datr',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': 'r7wjX4OG98nuAbxrNJgneO1C', 'id': 0},
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'fr',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0',
     'value': '1cj4Qa9Sk1YMXqwYX.AWUA8y3d7uCLVJr93sGtVEwyt2o.BfI7yp.PH.AAA.0.0.BfI7yv.AWVyQvlU', 'id': 0},
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'sb',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': 'qbwjX4Pctjqk_HOqWM7V7ABK', 'id': 0},
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'spin',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0',
     'value': 'r.1002447912_b.trunk_t.1596177579_s.1_v.2_', 'id': 0},
    {'domain': '.facebook.com', 'expirationDate': 1596177585, 'hostOnly': False, 'httpOnly': False, 'name': 'xs',
     'path': '/', 'secure': False, 'session': True, 'storeId': '0',
     'value': '13%3AhABzjDHMSkFDdg%3A2%3A1596177578%3A-1%3A-1', 'id': 0}]
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
