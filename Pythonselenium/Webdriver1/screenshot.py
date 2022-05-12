'''
---------------------------
File Name:screenshot
Author:FENGXIN
date:2022/3/16-20:48

---------------------------

'''

'''
网页截图操作
案例：分别打开我要自学网页面和百度页面，然后进行截图

'''
from selenium import webdriver
from time import sleep

# 加载浏览器驱动
driver = webdriver.Firefox()

# 打开自学网页面并截图
driver.get("http://www.51zxw.net")
driver.get_screenshot_as_file(r"C:\Users\FENG\Desktop\pytest\51zxw.jpg")

# 打开百度页面并截图
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r"C:\Users\FENG\Desktop\pytest\baidu.png")

sleep(2)
driver.quit()
