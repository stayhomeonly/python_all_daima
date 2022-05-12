'''
---------------------------
File Name:Call_loginPara
Author:FENGXIN
date:2022/3/18-9:49

---------------------------

'''
from selenium import webdriver
from Loginclass_para import *
from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost/")
driver.implicitly_wait(10)

Login().user_login(driver, "FENGXIN", "123456")
sleep(3)
Login().user_loginout(driver)
sleep(3)

Login().user_login(driver, "FENGXIN1", "123456")
sleep(3)
Login().user_loginout(driver)
sleep(3)

driver.quit()
