'''
---------------------------
File Name:testlogin
Author:FENGXIN
date:2022/1/15-10:14

---------------------------

'''
"""
特点：
文件名以test_开头的或者_test结尾的py文件
以test_开头的函数
以Test开头的类
以test_开头的方法（与2类似）
要注意的是所有的包必须要有init.py文件(在使用各种编辑器时会自动生成)
fixture：
与python自带的unittest测试框架中的setup、teardown类似，
pytest提供了fixture函数用以在测试执行前和执行后进行必要的准备和清理工作。
但是fixture函数对setup和teardown进行了很大的改进。
@pytest.fixture(scope=’Function、class、module、session’，auto=False)
scope参数：执行范围，
    function：每个test都运行，默认是function的scope 范围
    class：每个class的所有test只运行一次
    module：每个module的所有test只运行一次
    session：每个session只运行一次

注意：yield的使用
调用fixture的三种方式：
方式一：fixture的名字直接作为测试用例的参数
方式二：每个函数或者类前使用@pytest.mark.usefixtures('fixture')装饰器装饰
方式三：指定fixture的参数autouse=True这样每个测试用例会自动调用fixture


"""
import pytest

# 函数
# def test_login():
#     print("登录测试  函数")
#     assert 5 == 4
#
#
# def test_register():
#     print("注册测试  函数")

# 在Terminal 中，点击local,-s代表运行 显示程序中的print / logging输出
# 函数和方法最大的区别在参数，还有类里面叫做的方法，类外面叫做函数
"""
# 所有用例都执行的方法
"""

# class TestLogin:
#     # 所有用例都执行的方法
#     @pytest.fixture(scope='function', autouse=True)
#     def settear(self):
#         print('测试用例执行之前....链接数据库')
#
#         yield  # 类似于teardown
#
#         print("测试用例执行之后....关闭数据库")
#
#     def test_login(self):
#         print("登录测试  函数")
#
#     def test_register(self):
#         print("注册测试  函数")

'''
如果只想执行某个方法的情况自动链接数据库，关闭数据库的情况
只需要在函数后面加一个参数(设置的settear)
'''


class TestLogin1:

    @pytest.fixture()
    def settear(self):
        print('测试用例执行之前....链接数据库')

        yield

        print("测试用例执行之后....关闭数据库")

    def test_login(self, settear):
        print("登录测试  函数")

    def test_register(self):
        print("注册测试  函数")


'''
如果只想执行某个方法的情况自动链接数据库，关闭数据库的情况
另外一种方法
'''


class TestLogin2:

    @pytest.fixture()
    def settear(self):
        print('测试用例执行之前....链接数据库')

        yield

        print("测试用例执行之后....关闭数据库")

    @pytest.mark.usefixtures('settear')
    def test_login(self, settear):
        print("登录测试  函数")


    def test_login2(self):
        print("登录测试2  函数")


'''
自定义mark：
通过@pytest.mark控制需要执行哪些feature的test。
在pytest当中，先给用例打标记，在运行时，通过标记名来过滤测试用例。
注册标记：
创建一个pytest.ini文件
写入：
[pytest]
markers=
    me:
    you:
使用标记：
在 测试用例的前面加上：@pytest.mark.已注册标签名
如果只想运行被标记的方法：pytest -m 加上标记的标签（比如自己ini文件的age等等）

'''
