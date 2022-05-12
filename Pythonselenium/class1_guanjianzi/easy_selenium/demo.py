"""
#@Time：2022/5/7-19:10
#@file：demo.py
#@Project:Pythonselenium
#@Content:

"""
from time import sleep

from selenium.webdriver.common.by import By

'''
最简单的自动化的脚本
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.find_element(By.ID, 'kw').send_keys('虚竹')

driver.find_element(By.ID,'kw').send_keys('虚竹')
driver.find_element(By.ID, 'su').click()
sleep(3)
driver.quit()
