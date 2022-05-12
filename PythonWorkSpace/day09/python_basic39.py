"""
=========================
File Name:python_basic39
Author:pengyumei
Date:2021/11/27-17:08
==========================
"""

''''
魔法方法
构造方法:方法名__init__()会在创建类的对象时候自动调用,利用该特性我们可以在创建实例对象
的同时做一些操作

一般写一个类,如果不声明__init__方法时会自动使用默认的,默认的构造方法一般不显示,如果声明了
__init__方法,会覆盖默认的
注意:不能同时由两个__init__方法
'''


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2580

    # def __init__(self):  # 在创建Emp类的实例对象时,python会自动调用Emp类的__init__函数,当
    #     # 我们重写了以后,会自动完成我们的预期操作
    #     print('构造函数,在创建实例对象是自动调用')

    def __init__(self, no, name, sal):  # 重写了__init__方法,要求在创建实例对象的时候传入3个参数,并且绑定的实例对象的3个实例
        self.emp_no = no
        self.emp_name = name
        self.emp_sal = sal



# emp01 = Emp() #创建了一个Emp类的实例对象,没有重写__init__方法时,使用默认的__init__方法
# emp02 = Emp()

# emp03 = Emp(1001, 'scott', 5000)
# print(emp03.emp_no, emp03.emp_name, emp03.emp_sal)  # 1001 scott 5000

print(dir(Emp))  # 打印Emp类中所有的属性和方法
print(dir(str))
