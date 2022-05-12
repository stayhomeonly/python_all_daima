'''
---------------------------
File Name:frame_test
Author:FENGXIN
date:2022/3/12-18:15

---------------------------

'''

"""
frame嵌套页面元素定位,案例：在Frame.html文件种定位搜狗搜索页面，进行搜索操作。
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# 设置网页文件路径，r代表路径转义
file_path = r"C:\Users\FENG\Desktop\Frame.html"

driver.get(file_path)
# 切换到frame页面内
driver.switch_to.frame("search")
# 定位到搜索框按钮输入关键词
driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(5)
driver.find_element_by_css_selector("#stb")

sleep(2)
driver.quit()
