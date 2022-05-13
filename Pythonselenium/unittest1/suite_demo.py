"""
#@Time：2022/4/26-11:35
#@file：suite_demo
#@Project:Pythonselenium

"""
import os
import unittest
from HTMLTestRunner import HTMLTestRunner

from unittest1.study import TestLogin

# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例,第一种方法
# suite.addTest(TestLogin('test_03'))
# suite.addTest(TestLogin('test_6'))
# suite.addTest(TestLogin('test_7')) # 这种需要一个一个的添加

# 添加测试用例 第二种方法
cases = [TestLogin('test_6'), TestLogin('test_7')]
# suite.addTests(test_cases)

# 添加测试用例 第三种方法
# test_dir='./'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='study*.py')
# 第三种方法最后runner.run(discover)

# 添加测试用例，第四种方法
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))

# 添加测试用例，第五种方法
# suite.addTests(unittest.TestLoader().loadTestsFromName('unittest1.study.TestLogin'))

# 基于Runner来运行测试套件

# runner = unittest.TextTestRunner()
# runner.run(suite)

# 集成测试报告
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
# 保存路径
report_path = './report/'
report_file = report_path + 'report.html'
# 判断文件夹是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
# HTMLTestRunner的使用
with open(report_file, 'wb') as report:
    suite.addTests(cases)
    runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    runner.run(suite)
