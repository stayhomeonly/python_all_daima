'''
---------------------------
File Name:demo4
Author:FENGXIN
date:2022/3/20-12:36

---------------------------

'''
# 1、打开谷歌
# 2、访问网址
# 3、选中单选框中的桃子
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("")
# 单选框
# driver.find_element_by_css_selector("input[value='peach']")

# 1、打开谷歌
# 2、访问网址
# 3、只选中复选框中的桃子 思路：把选中的元素在点击一下 改为取消状态，在点击要选择的元素

# 1、获得到有checked属性的元素  选中的元素都会获得到
elements = driver.find_elements_by_css_selector("input[checked='checked']")
for element in elements:
    element.click()

# 就变成了取消的状态  点击要选择的元素  如果元素一样，要根据父级来定位，桃子  id 用#    class 用.
driver.find_element_by_css_selector("#s_checkbox input[value='peach']")

# 1、打开谷歌
# 2、访问网址
# 3、下拉框只选中桃子

# Select导包
# 三种方式定位
# 1、索引的方式  2 value值  3、文本值


# 先定位位置，在根据索引来选择
Select(driver.find_element_by_id("aoe")).select_by_index('1')
# 先定位位置，value值
Select(driver.find_element_by_id("aoe")).select_by_value('peach')
# 先定位位置，文本值
Select(driver.find_element_by_id("aoe")).select_by_visible_text('香蕉')


# 等待几秒中
sleep(3)

# 关闭浏览器

driver.quit()