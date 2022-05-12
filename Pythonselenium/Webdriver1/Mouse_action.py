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
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys("python")
# # # 获取搜索框元素对象
# element = driver.find_element(By.XPATH,'//input[@id="kw"]')
#
# sleep(3)
# # 双击操作
# ActionChains(driver).double_click(element).perform()
#
# sleep(2)
#
# # 右击操作
# ActionChains(driver).context_click(element).perform()
#
# sleep(3)

# 鼠标悬停
driver.implicitly_wait(3)
mouse= driver.find_element(By.XPATH,'//span[@id="s-usersetting-top"]')

# above.click()
sleep(3)
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element(By.XPATH,'//span[text()="高级搜索"]').click()
sleep(4)
driver.quit()
