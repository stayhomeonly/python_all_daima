"""
=========================
File Name:python_basic47
Author:pengyumei
Date:2021/11/29-11:43
==========================
"""
user = {'username': 'xiaohua', 'password': 'a123456'}


# 注册接口
def register(username, password, re_password):
    if len(username) == 0:
        return {'code': 1001, 'msg': '登录名不能为空'}
    elif len(password) == 0:
        return {'code': 1002, 'msg': '密码不能为空'}
    elif len(password) == 0:
        return {'code': 1003, 'mag': '确认密码不能为空'}
    elif 6 <= len(username) < 18 and 6 <= len(password) <= 18:
        return {'code': 1004, 'msg': '用户名和密码位数不正确'}
    elif password != re_password:
        return {'code': 1005, 'msg': '两次密码输入不一致'}
    elif username == user.get(username):
        return {'code': 1006, 'msg': '用户名已经存在'}
    else:
        return {'code': 9999, 'msg': '注册成功'}


# 登录接口
def login(username, password):
    if len(username) == 0:
        return {'code': 2001, 'msg': '登录名不能为空'}
    elif len(password) == 0:
        return {'code': 2002, 'msg': '密码不能为空'}

    elif 'usename' == user.get('username') and 'password' != user.get('password'):
        return {'code': 2004, 'msg': '用户名或密码不正确'}
    elif 'usename' != 'xiaohua' and 'password' == 'a123456':
        return {'code': 2004, 'msg': '用户名或密码不正确'}
    else:
        return {'code': 8888, 'msg': '登录成功'}
