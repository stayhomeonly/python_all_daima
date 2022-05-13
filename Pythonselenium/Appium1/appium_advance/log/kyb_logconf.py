'''
---------------------------
File Name:capability
Author:FENGXIN
date:2022/4/22-16:46

---------------------------

'''
import logging
import logging.config
from time import sleep

import yaml
from appium import webdriver
#
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

file = open('../yaml/desired_caps.yaml', 'r', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)

CON_LOG='log.conf' # 根据自己实际配置的文件路径来写
logging.config.fileConfig(CON_LOG) # 读取日志表
logging=logging.getLogger()# 日志采集器



desired_caps = {}
desired_caps['platformName'] = data['platformName']

desired_caps['platformVersion'] = data['platformVersion']
desired_caps['automationName']=data['automationName'] # 这个一定要加，不然定位不了
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['noReset'] = data['noReset']

desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']

logging.info('start app....')
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)


def check_cacelBtn():
    logging.info('check cacelBtn')
    try:
        cacelBtn = driver.find_element(By.ID,'android:id/button2')
    except NoSuchElementException:
        logging.info("no cacelBtn")
    else:
        cacelBtn.click()


check_cacelBtn()
sleep(2)


def check_skipBtn():
    logging.info('check skipBtn')

    try:
        skipBtn = driver.find_element(By.ID,'com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info("no skipBtn")
    else:
        skipBtn.click()


check_skipBtn()


