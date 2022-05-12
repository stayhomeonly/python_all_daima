'''
---------------------------
File Name:Browser_action
Author:FENGXIN
date:2022/3/5-13:38

---------------------------

'''
from selenium import webdriver
from time import sleep

# 加载浏览器

driver = webdriver.Firefox()

# 打开页面
driver.get("http://www.51zxw.net")
driver.maximize_window()  # 最大化窗口
sleep(2)

driver.get("https://www.51zxw.net/Show.aspx?cid=615")
driver.set_window_size(800, 800)  # 设置窗口长和宽
driver.refresh()  # 刷新页面
sleep(2)

driver.back() #返回页面
sleep(2)

driver.forward() # 前进一步

driver.close()