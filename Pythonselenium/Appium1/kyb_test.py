'''
---------------------------
File Name:kyb_test
Author:FENGXIN
date:2022/4/16-12:49

---------------------------

'''
from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'  # 设备名称

# 模拟器设备
desired_caps['deviceName'] = '127.0.0.1:62001'  # 连接设备
desired_caps['platforVersion'] = '7.1.2'

# mx4真机
# desired_caps['platformVersion']='5.1'
# desired_caps['deviceName']='MX4'
# desired_caps['udid']='750BBKL22GDN' # 同时脸上模拟器和真机要加上这一个参数，750BBKL22GDN是真机序列号


desired_caps['app'] = r'D:\kaoyan3.1.0.apk'
desired_caps['agePackages'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
print(desired_caps)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
