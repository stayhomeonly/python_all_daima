"""
=========================
File Name:python_senior31
Author:冯鑫
Date:2021/12/3-14:56
==========================
"""
'''
自动化分为三种:  
1.接口自动化
2.ui自动化
3.appium
python常见的自动化测试框架:
1.unittest : python自带的官方库，单元测试框架
2.pytest :　基于unittest开发，更好用更简单更强大
3.nose
'''

import requests

# 1、正确流程
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={'username': 'xiaowang', 'password': 'a123456'})
res_body = response.json()
print(res_body)  # {'code': 9999, 'msg': '登录成功'}

# 2、用户名错误
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={'username': 'xiaoniu', 'password': 'a123456'})
res_body = response.json()
print(res_body)  # {'code': 1003, 'msg': '用户名或密码错误'}

#  3、用户名为空
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={'username': '', 'password': 'a123456'})
res_body = response.json()
print(res_body)  # {'code': 1001, 'msg': '用户名不能为空'}

#  4、密码错误
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={'username': 'xiaowang', 'password': 'a1234567'})
res_body = response.json()
print(res_body)  # {'code': 1003, 'msg': '用户名或密码错误'

#  5、密码为空
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={'username': 'xiaowang', 'password': ''})
res_body = response.json()
print(res_body)  # {'code': 1002, 'msg': '密码不能为空'}
