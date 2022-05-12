'''
---------------------------
File Name:Keyword_actions
Author:FENGXIN
date:2022/3/11-22:08

---------------------------

'''
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector("#kw").send_keys("python")
sleep(2)
# 全选
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, "a")
sleep(2)
# 复制或者剪切
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, "c")
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, "x")

driver.get("http://www.sogou.com")
sleep(2)
# 粘贴关键字
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL, "v")
sleep(2)

driver.find_element_by_css_selector("#stb").click()
sleep(2)

driver.quit()
