"""
#@Time：2022/5/15-12:51
#@file：desired_caps
#@Project:python_basic05.py
#@Content:

"""
import logging
import logging.config
from time import sleep

import yaml
from appium import webdriver
#
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



CON_LOG='../log/log.conf' # 根据自己实际配置的文件路径来写
logging.config.fileConfig(CON_LOG) # 读取日志表
logging=logging.getLogger()# 日志采集器


def appium_desired():
    file = open('../yaml/desired_caps.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']

    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['automationName']=data['automationName'] # 这个一定要加，不然定位不了
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']
    # 如果输入中文字段，这个就是必须要写的，如果没有可以不写
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    logging.info('start app....')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    sleep(2)

    return driver
if __name__ == '__main__':
    appium_desired()