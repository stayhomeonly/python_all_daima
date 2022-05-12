'''
---------------------------
File Name:demo_1
Author:FENGXIN
date:2022/4/1-11:22

---------------------------

'''
from time import sleep

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

'''
driver驱动
drag_and_drop_offset  鼠标操作事件
ActionChains(driver).drag_and_drop_by_offset(元素).perform()
元素：被操作的元素
perform:要提交的操作


'''

# # 打开浏览器，并加载项目地址
# driver = webdriver.Chrome()
# driver.get("https://passport.ctrip.com/user/reg/home")  # 携程
# sleep(2)
#
# # 点击同意并继续
# driver.find_element_by_xpath('//a[@class="reg_btn reg_agree"]').click()
#
# # 定位滑块的位置
# element_hk = driver.find_element_by_xpath('//i[@class="cpt-logo cpt-img-double-right"]')
# print(element_hk.size)
# print(element_hk.size["height"], element_hk.size['width'])
# # ActionChains.drag_and_drop_by_offset(原始元素，鼠标对元素拖动另外一元素的x坐标，
# # 鼠标对元素拖动另外一元素的y坐标)
#
# # 定位滑块条的位置
# element_hktiao = driver.find_element_by_xpath('//div[@class="cpt-bg-bar"]')
# print(element_hktiao.size["height"], element_hktiao.size['width'])
# sleep(2)
#
# # 实现滑块操作
# x_location = element_hk.size['width'] + element_hktiao.size['width']
# y_location = element_hktiao.size['height']
# ActionChains(driver).drag_and_drop_by_offset(element_hk, x_location, y_location).perform()


# 鼠标移动的操作
driver2=webdriver.Chrome()
driver2.get("http://www.taobao.com")
sleep(2)

# 鼠标移动到中国大陆元素上
element_1=driver2.find_element_by_xpath('//span[@class="site-nav-region"]')
ActionChains(driver2).move_to_element(element_1).perform()

element_2 =driver2.find_element_by_xpath('//li[text()="中国台湾"]')
element_2.click()