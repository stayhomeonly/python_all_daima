'''
---------------------------
File Name:Call_login
Author:FENGXIN
date:2022/3/17-20:27

---------------------------

'''
from Loginclass import *
from selenium import  webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("http://localhost/")
driver.implicitly_wait(10)

Login().user_login(driver)
sleep(3)

Login().user_loginout(driver)
sleep(3)

driver.quit()
