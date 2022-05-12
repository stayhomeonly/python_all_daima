"""
--------------------------------
@Time  : 2022/2/24-------11:20
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
"""
ini文件改写了默认方式，将-vs改成了默认方式，每次运行都会执行
-m表示为测试用例添加标记，并且指定运行某个标记，可以加在类和方法上
2，需要在当前目录下创建pytest.ini文件，并且添加标记到ini文件中
常用的pytest.ini文件修改pytest的默认行为：
1，addopts=-vs:addopts参数可以更改默认命令选项
2,marks=test01,注册标记选项，注册后可以使用装饰器@pytest.mark.xxx装饰类或者函数
3，修改或者添加pytest的用例收集规则
python_files=test_*,*_test;测试文件以test_或者_test
pythone_classes=Test,测试类用Test开头并且不能有构造方法
python_functionsd=test,以test_开头
"""
import requests
import pytest


class TestLogin(object):
    @pytest.mark.test01
    def test_login01(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": "ab12345"})
        res = response.json()
        assert {'code': 9999, 'msg': '登录成功'} == res

    @pytest.mark.test02
    def test_login02(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "",
                                       "password": "ab12345"
                                       })
        res = response.json()
        assert {'code': 1001, 'msg': '用户名不能为空'} == res

    @pytest.mark.test02
    def test_login03(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laojkkk",
                                       "password": "ab12345"
                                       })
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    @pytest.mark.test03
    def test_login04(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": ""
                                       })
        res = response.json()
        assert {'code': 1002, 'msg': '密码不能为空'} == res

    @pytest.mark.test03
    def test_login05(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": "a312345"
                                       })
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res


if __name__ == '__main__':
    # pytest.main(['-m test02', './test_python02pytest.py'])#执行当前目录下标记为test02的用例
    # pytest.main(['-m not test01','./test_python02pytest.py'])#执行当前目录下标记不是test01的用例
    pytest.main(['-m test01 or test03', './test_python02pytest.py'])  # 执行当前目录下标记是test01和test03的用例
