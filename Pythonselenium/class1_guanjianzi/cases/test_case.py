"""
#@Time：2022/5/8-20:47
#@file：test_case
#@Project:Pythonselenium
#@Content:

"""
from time import sleep

from selenium.webdriver.common.by import By

from class1_guanjianzi.ui_key.webui_key import WebKeys

# 基于关键字驱动类进行测试
wk = WebKeys('Chrome')
wk.open('http://www.baidu.com')
wk.input(By.ID, 'kw','虚竹')
sleep(2)
wk.click(By.ID, 'su')
wk.wait(3)
wk.quit()
