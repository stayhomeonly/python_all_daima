'''
---------------------------
File Name:wangyiyun
Author:FENGXIN
date:2022/4/9-21:31

---------------------------

'''
from selenium import webdriver
from time import sleep

# 加载浏览器
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 加载地址
driver.get("https://music.163.com/")
driver.maximize_window()
# 定位登录，并且点击
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//a[text()="登录"]').click()
sleep(2)
# 选择其他登录模式，并且点击
driver.find_element(By.XPATH, '//a[text()="选择其他登录模式"]').click()
sleep(2)
# 点击同意
driver.find_element(By.XPATH, '//input[@id="j-official-terms"]').click()
sleep(2)
# 点击网易邮箱账号登录
driver.find_element(By.XPATH, '//a[text()="网易邮箱帐号登录"]').click()
# 输入登录账号
driver.find_element(By.XPATH, '//input[@class="_2dOybAah"]').send_keys('m15161039042@163.com')
# 输入密码
driver.find_element(By.XPATH, '//input[@class="sR89MU1J"]').send_keys('FENG1234.')
# 点击登录
driver.find_element(By.XPATH, '//div[text()="登录"]').click()

sleep(2)

driver.quit()
