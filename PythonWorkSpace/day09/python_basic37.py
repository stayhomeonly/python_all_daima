"""
=========================
File Name:python_basci37
Author:冯鑫
Date:2021/11/26-17:59
==========================
"""
'''
知识点：类属性分为：类属性和实列属性
        1、类属性声明在类体中，类属性时每个实例对象共同享有的属性，类属性可以通过 类名.属性名 直接访问
        2、实列属性，在创建对象之后声明的属性，该属性是某个对象独有的属性，只能通过对象去调用
        
'''


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 0
    __emp_age = 0  # 如果属性前有__,代表是私有属性，只能在该类中使用

    # 计算年薪
    def year_sal(self):
        return self.emp_sal * 12

    # 计算请假天数扣款
    def fine(self, day):
        return self.emp_sal / 22 * day

    print(__emp_age)  # 私有属性只能在类的内部访问


Emp.emp_sal = 2580  # 类属性可以通过，类名.属性名 直接访问 ，我们可以在类的外面修改类属性的值
# print(Emp.__emp_age)

emp01 = Emp()
print(emp01.emp_sal)  # 2580

print(emp01.year_sal())  # 30960

emp02 = Emp()
print(emp02.emp_sal)  # 2580
