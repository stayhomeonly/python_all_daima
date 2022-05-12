'''
---------------------------
File Name:Mouse_action
Author:FENGXIN
date:2022/3/10-18:58

---------------------------

'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# •	需要引入ActionChains类
# •	然后定位相关元素
# •	在ActionChains().调用相关鼠标操作方法

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.maximize_window()

driver.find_elements_by_css_selector("#kw")
