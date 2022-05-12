'''
---------------------------
File Name:Cookie_login
Author:FENGXIN
date:2022/3/17-11:29

---------------------------

'''
'''
案例：使用Cookie绕过百度验证码自动登录账户。
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({'name': 'BAIDUID', 'value': '515A98F7B04A154E9C622AE4EB4ECBD1:FG=1'})
driver.add_cookie({'name': 'BDUSS',
                   'value': 'kJHfmt0b2ZFc1NlamQxdn4tZm84cFlrczVvfkNLUDlYRHBJa2NnSlBQemdOMXBpRVFBQUFBJCQAAAAAAAAAAAEAAACr7As-t-u089Kv0q~SrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOCqMmLgqjJiT'})
sleep(3)
driver.refresh()
sleep(3)
driver.quit()
