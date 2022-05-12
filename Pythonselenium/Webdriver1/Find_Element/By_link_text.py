'''
---------------------------
File Name:By_link
Author:FENGXIN
date:2022/3/5-17:55

---------------------------

'''
from selenium import webdriver

from time import sleep

# link_text定位就是根据超链接文字进行定位。

driver = webdriver.Firefox()

driver.get("http://www.51zxw.net")
driver.find_element_by_link_text("程序开发").click()
sleep(3)

driver.find_element_by_partial_link_text("Selenium自动化测试教程").click()
sleep(3)



driver.quit()
