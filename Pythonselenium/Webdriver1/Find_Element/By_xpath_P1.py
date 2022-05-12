'''
---------------------------
File Name:By_xpath_P1
Author:FENGXIN
date:2022/3/5-20:28

---------------------------

'''
from selenium import webdriver

from time import sleep

# link_text定位就是根据超链接文字进行定位。

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
# 绝对路径，不建议用
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input")\
#     .send_keys("Selenium")

# 利用元素熟悉定位--定位到input标签中为kw的元素
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")

# 定位所有标签元素中，class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Python3")


# # 定位input标签中name属性为wd的元素
# driver.find_element_by_xpath("//input[@name='wd']").send_keys("51zxw")
sleep(2)

driver.find_element_by_id('su').click()
sleep(2)

driver.quit()