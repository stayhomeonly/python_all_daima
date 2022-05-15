"""
#@Time：2022/5/14-10:27
#@file：constants
#@Project:Pythonselenium
#@Content:

"""
# 获取项目路径
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)

# 配置文件所在路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')
# print(CONF_DIR)
CONF_FILE = os.path.join(CONF_DIR, 'config.ini')
# print(CONF_FILE)