# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""
# 1、pytest 安装
# pip install -U pytest
# >pytest --version 查看 pytest版本
'''
使用 pytest.mark.parametrize(argnames, argvalues) 参数化测试
'''

import pytest

# @pytest.mark.parametrize("arg_1", [4399, 2012])
# def test_add_by_func_aaa(arg_1):
#     print(arg_1)
#
#
# @pytest.mark.parametrize("arg_1, arg_2", [(4399, 'AAAA'), (2012, 'BBBB')])
# def test_add_by_func_aaa(arg_1,arg_2):
#     print("arg_1:{}  arg_2:{}".format(arg_1, arg_2))

# # 运行9次 组合运行
# @pytest.mark.parametrize("arg_1", [4399, 2012, 1997])
# @pytest.mark.parametrize("arg_2", ['AAAA', 'BBBB', 'CCCC'])
# def test_add_by_func_aaa(arg_1, arg_2):
#     print("arg_1:{}  arg_2:{}".format(arg_1, arg_2))


cases = [{"case_data": '{"username": "xiaoniu", "password": "a123456"}', "exp": "{'code': 9999, 'msg': '登录成功'}"},
         {"case_data": '{"username": "xiaoniu1", "password": "a123456"}', "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "", "password": "a123456"}', "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
         {"case_data": '{"username": "xiaoniu", "password": "a1234567"}', "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "xiaoniu", "password": ""}', "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]


@pytest.mark.parametrize("case", cases)
def test_login(case):
    print("case_data:{}".format(case['case_data']))
    print("exp:{}".format(case['exp']))


if __name__ == '__main__':
    pytest.main(['-v', '-s', './test_py_03.py'])
