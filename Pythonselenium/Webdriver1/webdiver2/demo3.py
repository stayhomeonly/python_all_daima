'''
---------------------------
File Name:demo3
Author:FENGXIN
date:2022/3/20-10:38

---------------------------

'''
# 1、打开谷歌浏览器
# 2、访问百度
# 3、点击新闻的链接
# 4、在新闻窗口中输入selenium

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(3)

driver.find_element_by_link_text("新闻").click()
# 目的：切换到新窗口中去
# 1、把打开的所有的窗口的句柄都获取到
all_handles = driver.window_handles

# 窗口显示出来
for handle in all_handles:
    print(handle)  # 打印所有句柄
    # 切换到新的窗口

    driver.switch_to.window(handle)
    print(driver.title)  # 打印窗口标题
    # 判断到我想要进入的窗口  窗口的名称
    # 如果窗口的标题字符串是我要操作的窗口标题一样，就跳出循环，切换到新的窗口
    if '百度新闻' in driver.title:
        break

# 然后在新窗口的元素
driver.find_element_by_id("ww").send_keys("Selenium")
