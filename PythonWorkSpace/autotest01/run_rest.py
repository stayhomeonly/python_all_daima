"""
=========================
File Name:run_rest07
Author:冯鑫
Date:2021/12/6-17:18
==========================
"""
import unittest
from BeautifulReport import BeautifulReport
# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案例，添加到测试套件中)
suite = unittest.TestSuite()

# 2.3 添加整个目录下的测试类到测试套件中，注意：测试模块必须以test开头
loader=unittest.TestLoader()
suite.addTest(loader.discover(r'D:\PythonWorkSpace\autotest01\testcases'))

BeautifulReport(suite).report(description='接口测试报告',
                              filename='report',
                              report_dir=r'D:\PythonWorkSpace\autotest01\reports')
