'''
---------------------------
File Name:Save_Days
Author:FENGXIN
date:2022/3/7-20:46

---------------------------

'''
# 1.根据选项元素标签定位
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)

# 根据option标签来定位
driver.find_elements_by_tag_name('option')[1].click()
driver.find_element_by_css_selector("[value='2']").click()

sleep(2)
driver.quit()

# 2.使用Select类定位
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)
# 利用Select类来进行定位
select = Select(driver.find_element_by_css_selector("[name='CookieDate']"))

select.select_by_index(2)
select.select_by_visible_text("留一年")
select.select_by_value("1")

sleep(2)
driver.quit()
