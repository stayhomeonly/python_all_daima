'''
---------------------------
File Name:by_list
Author:FENGXIN
date:2022/4/25-15:08
@Project : Pythonselenium


---------------------------

'''
from time import sleep

from selenium.webdriver.common.by import By

from Appium1.find_element.capability import driver

driver.find_element(By.ID, 'com.tal.kaoyan:id/login_register_text').click()

driver.find_element(By.ID, 'com.tal.kaoyan:id/activity_register_userheader').click()

images = driver.find_elements(By.ID,'com.tal.kaoyan:id/item_image')
print(images)
images[0].click()
sleep(2)
driver.find_element(By.ID, 'com.tal.kaoyan:id/save').click()  # 最后一步一直显示定位错误



