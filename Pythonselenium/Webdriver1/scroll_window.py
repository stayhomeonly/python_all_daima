'''
---------------------------
File Name:scroll_window
Author:FENGXIN
date:2022/3/15-20:30

---------------------------

'''
"""
滚动条控制操作
案例：打开我要自学网页面，然后将滚动条拖到最底部，然后再拖到顶部

"""

from selenium import webdriver

from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net")

js = "var action = document.documentElement.scrollTop = 10000"
driver.execute_script(js)
sleep(2)

js = "var action = document.documentElement.scrollTop = 0"
driver.execute_script(js)
sleep(2)

driver.quit()
