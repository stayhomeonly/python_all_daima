'''
---------------------------
File Name:implicitly_wait
Author:FENGXIN
date:2022/3/12-14:28

---------------------------

'''
from selenium import webdriver
from time import sleep, ctime

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)
driver.implicitly_wait(5)  # 隐式等待5秒

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("Python")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)

finally:
    print(ctime())

sleep(3)

driver.quit()
