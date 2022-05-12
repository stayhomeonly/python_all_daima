'''
---------------------------
File Name:capability
Author:FENGXIN
date:2022/4/22-16:46

---------------------------

'''

import yaml
from appium import webdriver

#
file = open('desired_caps.yaml', 'r', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)

desired_caps = {}
desired_caps['platformName'] = data['platformName']

desired_caps['platformVersion'] = data['platformVersion']
desired_caps['automationName']=data['automationName']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['noReset'] = data['noReset']

desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']

driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
