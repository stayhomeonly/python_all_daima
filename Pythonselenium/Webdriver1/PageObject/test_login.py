'''
---------------------------
File Name:test_login
Author:FENGXIN
date:2022/3/30-15:12

---------------------------

'''
from Webdriver1.PageObject.LoginPage import *
from selenium import webdriver

driver = webdriver.Firefox()

username = "15161039042"
password = '123456'

test_user_login(driver, username, password)
sleep(3)
driver.quit()
