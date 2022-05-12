'''
---------------------------
File Name:Cookie
Author:FENGXIN
date:2022/3/17-10:56

---------------------------

'''
'''
什么是Cookie
Cookie是储存在用户本地终端上的数据，实际上是一小段的文本信息。
Cookie作用
帮助 Web 站点保存有关访问者的信息，方便用户的访问。如记住用户名密码实现自动登录。

'''
from selenium import webdriver
from time import sleep
import pytest
driver = webdriver.Firefox()
driver.get("http://www.51zxw.net/")
# 获取cookie全部内容
cookie = driver.get_cookies()
print(cookie)
print(cookie[0])
# 添加cookie
driver.add_cookie({"name": "51zxw", "value": "www.51zxw.net"})
for cookie in driver.get_cookies():
    print("%s---%s" % (cookie['name'], cookie['value']))

driver.quit()




