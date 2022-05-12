'''
---------------------------
File Name:By_idName
Author:FENGXIN
date:2022/3/5-14:18

---------------------------

'''
from selenium import webdriver
from time import sleep
# id ,name 定位
# 加载浏览器
driver = webdriver.Firefox()

#打开百度首页
driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Selenium我要自学网")
driver.find_element_by_name("wd").send_keys("Selenium我要自学网")
sleep(2)

driver.find_element_by_id("su").click()
sleep(3)

driver.quit()
