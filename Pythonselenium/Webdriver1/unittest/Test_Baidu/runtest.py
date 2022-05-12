'''
---------------------------
File Name:run_test
Author:FENGXIN
date:2022/3/25-21:41

---------------------------

'''
# 执行测试用例
import unittest
from HTMLTestRunner import HTMLTestRunner

import time

test_dir = './test_case'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    report_dir = './test_report'
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_name = report_dir + '/' + now + 'result.html'

    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='Test Report', description='Tets case Result')
        runner.run(discover)

        f.close()
