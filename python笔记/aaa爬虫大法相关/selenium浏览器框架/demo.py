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
# chrome_options.add_argument('lang=zh_CN.UTF-8')
# 添加代理
# chrome_options.add_argument("--proxy-server=https://8.209.215.201:59394")
# 更换头部
chrome_options.add_argument(
    'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"')
# chrome_options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6'})
# 创建浏览器对象
browser = webdriver.Chrome(options=chrome_options)
# 设置中文

mainUrl = "https://www.facebook.com/"
# mainUrl = "http://whois.pconline.com.cn/"
# mainUrl = "https://m.facebook.com"
browser.get(mainUrl)
# print(f"browser text = {browser.page_source}")
# cookies = [
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'c_user',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': '100053838258303', 'id': 0},
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'datr',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': '0O4jX05G82EmRA-NRb4JLEMx', 'id': 0},
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'fr',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0',
#      'value': '1n6i2qqT0q10Mq9cY.AWUaVKB6PiOJGO2gRJOlrhLZ7Io.BfI-7L.0H.AAA.0.0.BfI-7Q.AWVqklTJ', 'id': 0},
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'sb',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0', 'value': 'y-4jXyoBFcvSx8wOTa_tF727', 'id': 0},
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'spin',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0',
#      'value': 'r.1002448666_b.trunk_t.1596190413_s.1_v.2_', 'id': 0},
#     {'domain': '.facebook.com', 'expirationDate': 1596190417, 'hostOnly': False, 'httpOnly': False, 'name': 'xs',
#      'path': '/', 'secure': False, 'session': True, 'storeId': '0',
#      'value': '24%3A5tN8y1oTghKFuQ%3A2%3A1596190412%3A-1%3A-1', 'id': 0}]
# for cookie in cookies:
#     browser.add_cookie(cookie)
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
# browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/bet/li').click()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/div/input').send_keys(
#     '008615990767710')
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[6]/div/button[1]').click()
# time.sleep(1)
# print(browser.get_cookies())
browser.get(mainUrl)
browser.quit()
