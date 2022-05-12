'''
---------------------------
File Name:new
Author:FENGXIN
date:2022/3/31-11:53

---------------------------

'''
from selenium import webdriver

from time import sleep

driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

a=driver.find_element_by_xpath('//span[@class="title-content-title"]')
sleep(2)
print(a.text)