"""
=========================
File Name:python_basic44
Author:pengyumei
Date:2021/11/27-18:03
==========================
"""

'''
1、多继承：一个子类可以继承多个父类
2、多继承的情况下，子类会先在自己类中去找需要的内容，找不到再去父类中去找
    该顺序按照__mro__提供的顺序去找（Method Resolution Orde）
'''


class Father(object):
    def f1(self):
        print('这是父类1')


class Mother(object):
    def f1(self):
        print('这是父类02')


class Baby(Father, Mother):
    pass


by = Baby()
by.f1()  # 这是父类1
print(Baby.__mro__)  # 查看方法解析顺序


# (<class '__main__.Baby'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)


# 菱形继承

class A:
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B, C):
    def test(self):
        print('from D')


dd = D()
dd.test()  # 查找顺序D、B、C、A、O
print(
    D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


# 钻石继承

class A:
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    def test(self):
        print('from F')


ff = F()
ff.test()  # 查找顺序，F/D/B/E/C/A/O从左向由，如果左边没有，就从右边重新开始
print(
    F.__mro__)  # (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)


# 查看继承父类__bases__
print(F.__bases__)  # (<class '__main__.D'>, <class '__main__.E'>)
print(D.__bases__)  # (<class '__main__.B'>,)

# isinstance()判断第一个参数是否是第二个参数的实例对象，返回bool类型
print(isinstance(123, int))  # True
print(isinstance(ff, F))  # True

# issubclass()判断第一个参数是否时第二个参数的派生类，返回bool类型
print(issubclass(F, A))  # True 不知直接的父类也是可以的
print(issubclass(F, D))  # True
