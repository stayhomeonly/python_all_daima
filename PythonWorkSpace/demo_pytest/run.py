'''
---------------------------
File Name:run.py
Author:FENGXIN
date:2022/1/20-21:10

---------------------------

'''
import os
import time
import allure


import pytest

if __name__ == '__main__':
    # pytest.main(['-vs'])
    # time.sleep(1)
    # os.system("allure generate  ../reports/tmp -o ../reports/html --clean")
    # pytest.main(['-vs', '-k', '001'])  # -k 表示执行后面所写的包含该内容的方法
    pytest.main(['-vs','--alluredir', 'report/allure_json', './'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')
