'''
---------------------------
File Name:user_login
Author:FENGXIN
date:2022/3/17-16:03

---------------------------

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost/")
sleep(3)

driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("FENGXIN")

driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('123456')

driver.find_element_by_name("Submit").click()
sleep(3)

driver.find_element_by_link_text("退出").click()
sleep(3)
driver.switch_to_alert().accept()

sleep(3)
driver.quit()

