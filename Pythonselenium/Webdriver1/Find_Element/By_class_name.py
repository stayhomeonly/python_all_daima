'''
---------------------------
File Name:By_class_name
Author:FENGXIN
date:2022/3/5-17:15

---------------------------

'''
from selenium import webdriver
from time import sleep

#class_name 定位

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_elements_by_class_name("s_ipt").send_keys("Selenium")
sleep(3)

driver.find_element_by_id("su").click()  # selenium 元素查找find_element_by_id方法，找到元素后进行点击
sleep(2)

driver.quit()
