'''
---------------------------
File Name:alert
Author:FENGXIN
date:2022/3/13-20:56

---------------------------

'''
"""
案例：点击百度首页设置按钮，然后进入搜索设置页面，点击“保存设置”或“恢复默认”按钮，处理警告弹窗窗口
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_xpath("//*[@class='s-top-right-text c-font-normal c-color-t s-top-right-new']").click()

sleep(2)

driver.find_element_by_link_text("搜索设置").click()
sleep(3)

driver.find_element_by_link_text("保存设置").click()
sleep(3)
# 处理警告窗口
alert = driver.switch_to_alert()
alert.accept()
sleep(2)

driver.quit()




