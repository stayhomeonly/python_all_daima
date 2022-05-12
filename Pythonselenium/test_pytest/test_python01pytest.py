"""
--------------------------------
@Time  : 2022/2/23-------16:58
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
"""
1,pytest的作用：用来管理和运行测试用例
2,pytest安装：pip install pytest(pip install -i 镜像源）
3,查看是否安装成功：pytest --version
4,测试用例编写：
    测试文件以test_开头或者以_test结束
    测试类以Test开头，并且不能有__init__等构造方法
    测试用例或者测试函数以_test开头
    断言使用基本的assert
5，常用的断言
    assert A==B
    assert A>B
    assert A in B
"""
import requests
import pytest


class TestLogin(object):
    def test_login01(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": "ab12345"})
        res = response.json()
        assert {'code': 9999, 'msg': '登录成功'} == res

    def test_login02(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "",
                                       "password": "ab12345"
                                       })
        res = response.json()
        assert {'code': 1001, 'msg': '用户名不能为空'} == res

    def test_login03(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laojkkk",
                                       "password": "ab12345"
                                       })
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    def test_login04(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": ""
                                       })
        res = response.json()
        assert {'code': 1002, 'msg': '密码不能为空'} == res

    def test_login05(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "laoliu",
                                       "password": "a312345"
                                       })
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res


# 密码区分大小写
def test_login06():
    response = requests.post(url="http://127.0.0.1:5000/user_login",
                             data={"username": "laoliu",
                                   "password": "Ab12345"
                                   })
    res = response.json()
    assert {'code': 1003, 'msg': '用户名或密码错误'} == res


if __name__ == '__main__':
    """
   # 知识点1，运行该模块下所有测试用例
    # pytest.main(['./test_python01pytest.py'])#运行指定模块
    # 知识点2，-s,-v,-k,-q的运用
    # pytest.main(['-v', './test_python01pytest.py'])  # 运行指定模块，-v表示详细输出执行用例
    # pytest.main(['-q', './test_python01pytest.py'])  # 静默模式只显示运行结果
    # pytest.main(['-s', './test_python01pytest.py'])  # 运行指定模块，显示用例中的打印和日志信息
    # 知识点3运行模块中的某个类
    # pytest.main(['./test_python01pytest.py::TestLogin'])#运行模块下的某个类
    # pytest.main(['-vs','./test_python01pytest.py::TestLogin'])#运行模块下的类，并详细执行用例，打印日志信息
    # 知识点3，运行某个模块下的某个用例
    # pytest.main(['-vs', './test_python01pytest.py::TestLogin::test_login04'])
    # 运行某个目录下的所有测试用例
    # pytest.main(['./'])#运行当前模块下所有的test_和_test用例
    # pytest.main([r'D:\Tools\workspacepython\pythonProject\day13\test_pytest'])#运行当前目录下所有的test_和_test用例
    # 只运行给定字符串表达式匹配的测试用例，比如匹配当前目录下包含包含login的用例(不区分大小写，不区分匹配目录，模块名，类名，用例名)
    # pytest.main(['-vs','-k login','./'])#执行指定类中所有包含login的用例
    """
