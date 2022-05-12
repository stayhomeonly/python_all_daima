# -- coding:utf-8 --

"""
============================
   Author:liucl
   date: 2021/12/13-23:12

pip list 看看安装后的所有库
https://www.jb51.net/article/154697.htm 控制台乱码 改为 gbk或者utf8

# 设置allure结果报告
# 1、解压 allure-2.17.1.zip
# 2、然后配置环境变量： 在系统变量path中添加D:\Program Files\allure-2.13.3\bin，然后确定保存。


# 下载 allure-pytest 插件，用来生成 Allure 测试报告所需要的数据。
# pip3 install allure-pytest

第一步：将测试数据打包

pytest 脚本目录 --alluredir 存放报告目录
第二步：生成测试报告

allure generate -o 运行结果目录 存放报告目录 --clean # 清空

# 第三步：pyChram要重新启动 加载 否则报： 找不到 allure
=============================
"""
import pytest,os
import allure




# 注意
if __name__ == '__main__':
    pytest.main(['--alluredir', 'report/allure_json','./'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')

