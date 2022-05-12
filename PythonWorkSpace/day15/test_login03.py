"""
=========================
File Name:test_login03
Author:冯鑫
Date:2021/12/4-17:06
==========================
"""
import unittest, requests
from ddt import ddt, data


# 反射

class Emp:
    emp_name = ''
    emp_sal = 0


emp01 = Emp()
emp01.emp_name = 'xiaohua'
emp01.emp_sal = 14000

# 利用反射动态的设置属性，只有在代码运行时，才给emp01对象设置属性
setattr(emp01, 'emp_no', 1001)  # setattr(对象名，属性名，属性值）
print(emp01.emp_no)  # 1001

# 利用反射动态获取属性值,getattr(对象名，属性名）
print(getattr(emp01, 'emp_name'))  # xiaohua
print(getattr(emp01, 'emp_sal'))  # 14000
print(getattr(emp01, 'emp_no'))  # 1001

# 利用反射 动态的删除属性,delatt(对象名,属性名)
delattr(emp01, 'emp_no')
# print(emp01.emp_no)# AttributeError: 'Emp' object has no attribute 'emp_no'


'''
将字典转换为对象
'''
dict1 = {"username": "xiaohua", "password": "a123456"}
print(dict1["username"])

print(dict1.items())  # 获取多有键值对，并且键值对存放在元组里返回 [('username', 'xiaohua'), ('password', 'a123456')]


class CaseData:
    def __init__(self, dict_case):
        for i in dict_case.items():  # 获取字典中的每一对键值对，并且进行遍历
            setattr(self, i[0], i[1])  # 动态的为实例对象赋值，username,xiaohua  password,a123456


cd = CaseData(dict1)

print(cd.username, cd.password)  # xiaohua a123456

# 将case中所有字典转换为对象，并且存到了一个列表中
cases = [{"case_data": "{'username': 'xiaowang', 'password': 'a123456'}", "exp": "{'code': 9999, 'msg': '登录成功'}"},
         {"case_data": "{'username': 'xiaoxu1', 'password': 'a123456'}", "exp": "{'code': 1003 ,'msg':'用户名或者密码错误'}"},
         {"case_data": "{'username': '', 'password': 'a123456'}", "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
         {"case_data": "{'username': 'xiaowang', 'password': 'a1234567'}", "exp": "{'code': 1003 ,'msg':'用户名或者密码错误'}"},
         {"case_data": "{'username': 'xiaowang', 'password': ''}", "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]

all_case = []
for i in cases:
    ca = CaseData(i)  # 把字典转换为对象
    all_case.append(ca)  # 把对象存放在列表中
print(all_case[4].case_data, all_case[4].exp)


# {'username': 'xiaowang', 'password': ''} {'code': 1002, 'msg': '密码不能为空'}

@ddt
class TestLogin(unittest.TestCase):  # 测试类需要继承unittest.TestCase,这是当前类就是测试类
    @data(*all_case)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data=eval(case.case_data))  # 识别()中的python表达式，把字符串转成了字典
        res_body = response.json()  # res_body就是接口响应的实际结果
        self.assertEqual(eval(case.exp), res_body)
