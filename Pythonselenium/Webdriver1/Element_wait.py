'''
---------------------------
File Name:Element_wait
Author:FENGXIN
date:2022/3/12-13:51

---------------------------

'''

"""
•	显示等待是针对某一个元素进行相关等待判定；
•	隐式等待不针对某一个元素进行等待，全局元素等待。
________________________________________
a.相关模块
•	WebDriverWait 显示等待针对元素必用
•	expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）
•	NoSuchElementException 用于隐式等待抛出异常
•	By 用于元素定位

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)

driver.find_element_by_css_selector("#kw").send_keys("Selenium 自学网")
# 显示等待--判断搜索按钮是否存在
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "su")))
# 如果By.ID 后面改掉，就会抛出异常
element.click()

sleep(3)

driver.quit()
