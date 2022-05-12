"""
=========================
File Name:constants
Author:冯鑫
Date:2021/12/9-11:16
==========================
"""
import os

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # __file__当前文件名,全部大写代表常量
# print(BASE_DIR)  # D:/PythonWorkSpace/autotest02

# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')
# print(CASE_DIR)  # D:/PythonWorkSpace/autotest02\testcases

# 测试数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'cases.xlsx')
# print(DATA_FILE)  # D:/PythonWorkSpace/autotest02\data\case.xlsx

# log所在路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')
INFO_DIR = os.path.join(LOG_DIR, 'info.log')
ERROR_DIR = os.path.join(LOG_DIR, 'error.log')

# 配置文件所在路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')
CONF_FILM = os.path.join(CONF_DIR, 'config.ini')

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
