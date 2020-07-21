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
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "http://47.112.147.225:3008/login?redirect=%2Fdashboard"
browser.get(mainUrl)
# print(f"browser text = {browser.page_source}")

browser.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('ykt007')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').send_keys('ykt007')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/div/input').send_keys(
    '008615990767710')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div/div[6]/div/button[1]').click()
time.sleep(1)
browser.quit()
