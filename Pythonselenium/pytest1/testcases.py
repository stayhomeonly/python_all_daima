"""
#@Time：2022/5/5-20:17
#@file：test_cases2
#@Project:python_basic05.py
#@Content:

"""
import pytest

'''
pytest中的用例管理手段：mark
可以通过mark装饰器对所有的用例进行标记，不同的标记区分进行管理
'''


@pytest.mark.webui
def vip_01():
    print('web01')


@pytest.mark.webui
def test_02():
    print('web02')


@pytest.mark.interface
@pytest.mark.temp
def test_03():
    print('interface01')


@pytest.mark.interface
def test_04():
    print('interface01')


if __name__ == '__main__':
    pytest.main()
    # 如果想单独运行某个案例：
    # pytest -s test_case2.py -m webui  运行webui的标签
    # 如果多个标签pytest -s test_case2.py -m webui,temp
