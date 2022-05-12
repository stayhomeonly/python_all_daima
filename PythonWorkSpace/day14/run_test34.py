"""
=========================
File Name:run_test34
Author:冯鑫
Date:2021/12/3-17:47
==========================
"""

import unittest
from day14.test_login32 import TestLogin

"""
使用测试套件管理和运行测试用例
好处：
1、可以自由的执行多个模块的测试类
2、可以配置图形化的结果报告
概念：测试套件： test suite：测试套件，用来把需要一起执行的测试用例集中放到一块执行，
相当于一个篮子。我们可以使用TestLoader来加载测试用例到测试套件中。
"""

# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案列，添加到测试套件中)
suite = unittest.TestSuite()

# 2、将测试用例添加到测试套件中
# 2.1 添加测试方法到测试套件
# suite.addTest(TestLogin('test_login02')) # 把TestLogin类下的test_login02测试用例添加到测试套件中
# suite.addTest(TestLogin('test_login03'))

# 2.2添加整个测试类到测试套件中
# loader = unittest.TestLodar()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin)) # 加载整个测试类到测试套件中


# 2.3 添加整个目录下的测试类到测试套件中，注意：测试模块必须以test开头
loader = unittest.TestLoader() # 添加测试用例,TestLoader相当于一个加载器
suite.addTest(loader.discover(r'D:\PythonWorkSpace\day14'))

# 3、获取runner 对象，并且调用run方法运行测试用例
runner=unittest.TextTestRunner
runner.run(suite) # 通过unittest的runner对象运行测试套件