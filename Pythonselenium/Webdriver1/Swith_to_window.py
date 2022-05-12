'''
---------------------------
File Name:Swith_to_window
Author:FENGXIN
date:2022/3/12-21:02

---------------------------

'''
"""
多窗口切换操作
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(2)

selenium_index = driver.current_window_handle  # 获得当前句柄
print(selenium_index)
sleep(2)

driver.find_element_by_partial_link_text("新闻").click()
sleep(2)

# 跳转到百度主页面，点击图片
driver.switch_to.window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text("图片").click()

sleep(3)
driver.quit()
