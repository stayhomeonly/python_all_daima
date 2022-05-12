"""
=========================
File Name:test_login02
Author:冯鑫
Date:2021/12/4-17:06
==========================
"""
import unittest, requests
from ddt import ddt, data

'''
ddt 可以在参数化测试数据，把不同的数据进行参数化，做到代码逻辑和测试数据分离
使用方法：
1、将测试类使用@ddt进行标记
2、将需要循环使用测试数据的测试方法，用@data进行标记
'''

cases = [{"case_data": "{'username': 'xiaowang', 'password': 'a123456'}", "exp": "{'code': 9999, 'msg': '登录成功'}"},
         {"case_data": "{'username': 'xiaoxu1', 'password': 'a123456'}", "exp": "{'code': 1003 ,'msg':'用户名或者密码错误'}"},
         {"case_data": "{'username': '', 'password': 'a123456'}", "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
         {"case_data": "{'username': 'xiaowang', 'password': 'a1234567'}", "exp": "{'code': 1003 ,'msg':'用户名或者密码错误'}"},
         {"case_data": "{'username': 'xiaowang', 'password': ''}", "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]


@ddt
class TestLogin(unittest.TestCase):  # 测试需要继承unittest.TestCase类，这是当前类就是测试类
    @data(*cases)  # 拆包，把值都赋给case
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data=eval(case["case_data"]))  # 识别()中的python表达式，把字符串转成了字典
        res_body = response.json()  # res_body就是接口响应的实际结果
        self.assertEqual(eval(case["exp"]), res_body)
