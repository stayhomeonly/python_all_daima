"""
=========================
File Name:python_basic43
Author:pengyumei
Date:2021/11/27-17:50
==========================
"""

'''
1、父类如果__init__方法，子类创建对象时，必须调用父类的__init__方法
2、父类如果__init__方法，子类也有__init__方法，这时候子类的__init__方法中，必须调用父类的__init__
方法
    格式：父类类名，__init__(入参1，入参2.....) 例如：Animal.__init__(self，country,name,age)
    
'''


class Animal:
    def __init__(self, country, name, age):  # __init__创建实例对象时被调用，也叫构造方法
        self.country = country
        self.name = name
        self.age = country


class Dog(Animal):
    def walk(self):
        print('子类的walk方法')


dog1 = Dog('美国', '斯派克', 5)  # 创建子类实例对象时，调用了父类的__init__方法
print(dog1.country, dog1.name, dog1.age)  # 美国 斯派克 美国


class Cat(Animal):
    def __init__(self, country, name, age, color):
        self.color = color
        Animal.__init__(self, country, name, age)  # 调用父类的构造方法,必须符合父类的要求


cat1 = Cat('美国', 'Tom', 5, 'blue')  # 子类有__init__方法时，这时候子类的__init__方法中，必须调用父类的__init__方法
print(cat1.country,cat1.name,cat1.age,cat1.color)#美国 Tom 美国 blue