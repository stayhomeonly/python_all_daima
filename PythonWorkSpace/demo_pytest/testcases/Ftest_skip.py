'''
---------------------------
File Name:test_skip
Author:FENGXIN
date:2022/1/16-14:22

---------------------------

'''
import pytest

'''
跳过用例mark：
skip和skipif可以标记无法在某些平台上运行的测试功能，或者您希望失败的测试功能。
要给跳过的测试添加理由和条件，应当使用skipif
使用skip和skipif标记，测试会直接跳过，而不会被执行。
@pytest.mark.skipif(condition)

@pytest.mark.skipif(tasks.__version__<'0.2.0',reason = 'not supported until version 0.2.0)
使用标记：
在 测试用例的前面加上：@pytest.mark.已注册标签名


'''


def test_01():
    print('test 01')


num1 = 9
num2 = 10


#@pytest.mark.skip(reason='跳过的原因'),可以用来直接跳过执行此方法
@pytest.mark.skipif(num1 < num2, reason='跳过的原因')  # 第一个入参是代表条件，只有成立或者不成立，也就是True或者
# False,第二个入参是原因
def test_02():
    print('test 02')


def test_03():
    print('test 03')


def data():
    return [('123456', '12345'), ('abc1234', 'abcdefg')]


'''
参数化mark：
允许在测试函数或类中定义多组参数
传入单个参数：
@pytest.mark.parametrize('参数名',lists)
传入两个参数：
@pytest.mark.parametrize('参数1,参数2',[(参数1_data[0],参数2_data[0]),(参数1_data[1],
参数2_data[1])]
    传三个或者更多也是这样传。list的每个元素都是一个元祖，元祖里的每个元素和按参数顺序一一对应。

'''


# 参数化就是为了让执行不同的数据，避免重复写代码

@pytest.mark.parametrize('username', ['123456', 'abc1234', 'abcdefg'])  # 单个参数的场景
def test_login(username):
    print(username)


@pytest.mark.parametrize('username,pwd', [('123456', '12345'), ('abc1234', 'abcdefg')])  # 两个个参数的场景
def test_login(username, pwd):
    print(username)
    print(pwd)


# 如果多个参数的场景,放在excel中

@pytest.mark.parametrize('username,pwd', data())  # 两个个参数的场景
def test_login(username, pwd):
    print(username)
    print(pwd)


'''
conftest.py文件：
配置里可以实现数据共享，不需要import就能自动找到一些配置。
conftest文件实际应用需要结合fixture来使用，fixture中参数scope也适用conftest中fixture的特性
'''
