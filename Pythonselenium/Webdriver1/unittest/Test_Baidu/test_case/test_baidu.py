'''
---------------------------
File Name:test_baidu
Author:FENGXIN
date:2022/3/25-21:01

---------------------------

'''
from selenium import webdriver
from time import sleep
import unittest


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()

    def test_baidu(self):
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys('Selenium自学网')
        driver.find_element_by_id("su").click()
        sleep(3)

        title = driver.title

        self.assertEqual(title, "Selenium自学网_百度搜索")

        driver.find_element_by_partial_link_text("Selenium IDE").click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
