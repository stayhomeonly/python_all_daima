'''
---------------------------
File Name:updoad_file
Author:FENGXIN
date:2022/3/14-21:00

---------------------------

'''

"""
上传文件
案例：在百度搜索上传本地图片进行搜索
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)

driver.find_element_by_css_selector(".soutu-btn").click()
sleep(2)

driver.find_element_by_css_selector(".upload-pic").send_keys(r"C:\Users\FENG\Desktop\shuiyin.png")

sleep(3)
driver.quit()
