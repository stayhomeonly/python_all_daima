"""
=========================
File Name:test.login32
Author:冯鑫
Date:2021/12/3-15:17
==========================
"""
import unittest, requests

'''
使用框架进行测试，解决自动比对
注意使用unittest框架的步骤：
    1、定义测试类，类名最好和被测接口匹配，并且测试类需要继承TestCase类
    2、所有测试方法必须以test开头
    3、我们可以使用断言对结果进行比对
'''


class TestLogin(unittest.TestCase):  # 测试类需要继承unittest.TestCase类，这时当前类就是测试类
    def test_login01(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={'username': 'xiaowang', 'password': 'a123456'})
        res_body = response.json()  # res_body就是接口响应的实际结果
        # assertEqual(A,B)  断言A和B是否相等，断言实际结果和预期结果是否相等
        self.assertEqual({'code': 9999, "msg": "登录成功"}, res_body)  # assert是断言的意思，Equal是相等的意思

    def test_longin02(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={'username': 'xiaoniu', 'password': 'a123456'})
        res_body = response.json()
        self.assertEqual({'code': 1003, 'msg':"用户名或者密码错误"}, res_body)

    def test_login03(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={'username': '', 'password': 'a123456'})
        res_body = response.json()
        self.assertEqual({'code': 1001, 'msg': '用户名不能为空'}, res_body)

    def test_login04(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={'username': 'xiaowang', 'password': 'a1234567'})
        res_body = response.json()
        self.assertEqual({'code': 1003, 'msg': '用户名或者密码错误'}, res_body)

    def test_login05(self):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data={'username': 'xiaowang', 'password': ''})
        res_body = response.json()
        self.assertEqual({'code': 1002, 'msg': '密码不能为空'}, res_body)
