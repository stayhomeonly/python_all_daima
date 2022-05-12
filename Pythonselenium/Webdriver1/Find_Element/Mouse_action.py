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

driver.find_element_by_css_selector("#kw").send_keys("Python")
sleep(3)
# 获取搜索框元素对象
element = driver.find_element_by_css_selector("#kw")

# 双击操作

ActionChains(driver).double_click(element).perform()
sleep(3)

# 右击鼠标
ActionChains(driver).context_click(element).perform()
sleep(3)

# 鼠标悬停
above = driver.find_element_by_css_selector(".pf")
sleep(3)
ActionChains(driver).move_to_element(above).perform
sleep(3)
driver.quit()