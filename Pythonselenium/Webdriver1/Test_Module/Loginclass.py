'''
---------------------------
File Name:Loginclass
Author:FENGXIN
date:2022/3/17-20:12

---------------------------

'''
from selenium import webdriver
from time import sleep


class Login():
    def user_login(self, driver):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("FENGXIN")

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys('123456')

        driver.find_element_by_name("Submit").click()

    def user_loginout(self, driver):
        driver.find_element_by_link_text("退出").click()
        sleep(3)
        driver.switch_to_alert().accept()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://localhost/")
    driver.implicitly_wait(10)

    Login().user_login(driver)
    sleep(2)
    Login().user_loginout(driver)
    sleep(2)
