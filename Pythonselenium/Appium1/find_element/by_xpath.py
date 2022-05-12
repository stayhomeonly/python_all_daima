'''
---------------------------
File Name:by_xpath
Author:FENGXIN
date:2022/4/23-19:47
@Project : Pythonselenium


---------------------------

'''

'''
/:从根节点选取。
//:从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
nodename:选取此节点的所有子节点
.:选取当前节点
..:选取当前节点的父节点
@:选取属性
*:匹配任何元素节点
@*:匹配任何属性节点
node():匹配任何类型的节点
'''
from Appium1.find_element.capability import driver

driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('fengxin1')

driver.find_element_by_xpath('//*[@class="android.widget.EditText"  and @index="3"]').send_keys('FENG1234')

driver.find_element_by_xpath('//android.widget.Button').click()

# driver.find_element_by_xpath('//*[@class="android.widget.Button"]')