"""
=========================
File Name:test_register37
Author:冯鑫
Date:2021/12/4-11:42
==========================
"""
''''
对注册接口进行测试
1、使用postman进行测试，并且保留测试数据
2、使用unittest进行测试
3、将案例天添加到测试套件中，并且生成html报告
'''

import unittest, requests
from day11.db_utils03 import DBUtils


class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    # 1、正确流程
    def test_register01(self):
        self.db.cud('delete from tb_user where name= %s;', ('xiaowang',))
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={'username': 'xiaowang',
                                       'password': 'a123456',
                                       're_password': 'a123456',
                                       'phone': '15998741235',
                                       'email': "11261@qq.com"})
        res_body = response.json()
        self.assertEqual({'code': 9999, "msg": '注册成功'}, res_body)

    # 2、用户名为空
    def test_register02(self):
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={'username': '',
                                       'password': 'a123456',
                                       're_password': 'a123456',
                                       'phone': '15998741235',
                                       'email': "11261@qq.com"})
        res_body = response.json()
        self.assertEqual({'code': 1001, 'msg': '登录名不能为空'}, res_body)

    # 3、密码为空
    def test_register03(self):
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={'username': 'xiaowang',
                                       'password': '',
                                       're_password': 'a123456',
                                       'phone': '15998741235',
                                       'email': "11261@qq.com"})
        res_body = response.json()
        self.assertEqual({"code": 1002, "msg": "密码不能为空"}, res_body)

    # 4、用户名已存在

    def test_register04(self):
        # 数据回滚
        self.db.cud("delete from tb_user where name =%s;",('xiaowang',))
        self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                    ('xiaowang','a123456','11265@qq.com','15998741236'))
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={'username': 'xiaowang',
                                       'password': 'a123456',
                                       're_password': 'a123456',
                                       'phone': '15998741236',
                                       'email': "11265@qq.com"})
        res_body = response.json()
        self.assertEqual({"code": 1010, "msg": "用户名已经被注册"}, res_body)
