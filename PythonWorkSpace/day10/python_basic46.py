"""
=========================
File Name:python_basic46
Author:pengyumei
Date:2021/11/29-11:43
==========================
"""
'''
封装：
第一层面的封装：把属性和方法 组合成一个类，就是简单的封装
第二层面的封装：类中把某些属性的方法隐藏起来(或者说定义为私有），只能在类中使用、外部无法访问，
或者留下少量的函数供外部访问

'''

# 小花这个学生
name = 'xiaohua'
sex = '女'
age = 20


# 声明三个变量去形容小花这个学生，有声明弊端
# 弊端：太零散，如果学生太多，需要不断的新建变量去描述

class Student(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


one = Student('老刘', '男', 38)
two = Student('老王', '男', 30)
three = Student('老徐', '男', 28)

print('姓名{},性别{},年龄{}'.format(two.name, two.sex, two.age))


# 第二层面的封装:控制访问权限
# 我们可以把所有属性设置为私有属性，不在允许对象访问
class Stu(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age


four = Stu('小花', '女', 20)


# print('姓名{},性别{},年龄{}'.format(four.name, four.sex, four.age))AttributeError: 'Stu' object has no attribute 'name'


# 问题来了：现在我们把name、age、sex设置为私有属性，但是我又想他们通过我指定的接口去访问或修改
# 我的属性，怎么办呢？

class Stu1(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# 这样有效的控制了访问、修改的权限，name,age允许访问和修改

five = Stu1('小李mini', '猛男', 25)
print(five.get_name(), five.get_age())  # 小李mini 25

five.set_age(26)
print(five.get_name(), five.get_age())  # 小李mini 26

five.set_name('小李plus')
print(five.get_name(), five.get_age())  # 小李plus 26


# 上面的素材太麻烦，我们可以使用装饰器：property(是属性，表示可以通过实例直接访问）和setter(代表设置属性值)
class Stu2(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


six = Stu2('易烊千玺', '男', 21)
six.name = 'TF男孩'
print('姓名是:', six.name)  # 姓名是: TF男孩
six.age = 22
print('姓名是{}，年龄{}'.format(six.name,six.age))#姓名是TF男孩，年龄22
