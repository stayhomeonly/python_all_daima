import pytest


@pytest.fixture(scope='function')
def func_scope():
    print('--在函数前使用--')
    yield  # 暂停的意思
    print('--在函数后使用--')


@pytest.fixture(scope='class',autouse=True)
def class_scope():
    print('--在类前使用')
    yield
    print('--在类后使用')
