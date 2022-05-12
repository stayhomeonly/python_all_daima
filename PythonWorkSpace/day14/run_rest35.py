"""
=========================
File Name:run_rest34
Author:冯鑫
Date:2021/12/3-18:09
==========================
"""

import unittest
from BeautifulReport import BeautifulReport

'''
HTML类型的结果报告
1、下载BeautifulReport包
2、在代码中引入
'''
# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案例，添加到测试套件中)
suite = unittest.TestSuite()

# 2.3 添加整个目录下的测试类到测试套件中，注意：测试模块必须以test开头
loader=unittest.TestLoader()
suite.addTest(loader.discover(r'D:\PythonWorkSpace\day14'))

# 3、使用BeautifulReport 运行测试套件
BeautifulReport(suite).report(description='test23班登录接口测试报告',
                              filename='report')






