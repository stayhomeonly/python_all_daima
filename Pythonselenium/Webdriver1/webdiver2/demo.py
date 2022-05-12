'''
---------------------------
File Name:demo
Author:FENGXIN
date:2022/3/19-17:40

---------------------------

'''
from selenium import webdriver
from time import sleep

# 打开126邮箱
driver = webdriver.Chrome()
driver.get("https://www.126.com/")
driver.maximize_window()

driver.implicitly_wait(10)

# 找不到元素，1看下有没有写错  复制的 2.检查有没有特殊元素 iframe
# 定位iframe里面，怎么做 id带有数字就不能用的
# 1、找到iframe,切换到iframe 内部中  //* 所有节点的元素  找到iframe的父亲
iframe1 = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
# 切换到iframe 内部中  swith_to.frame跳转
driver.switch_to.frame(iframe1)

element1 = driver.find_element_by_name("email")
element1.send_keys("m15161039042")
# 进入iframe内部l

# 想要进入到外部 iframe切回到主页面
# driver.switch_to.default_content()
# sleep(3)

# 点击二维码
# driver.find_element_by_id("lbApp").click()

driver.find_element_by_name("password").send_keys("FENG1234.")
sleep(3)
driver.find_element_by_id("dologin").click()
sleep(3)
driver.quit()
