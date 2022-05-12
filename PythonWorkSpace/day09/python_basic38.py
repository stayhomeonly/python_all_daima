"""
=========================
File Name:python_basic38
Author:冯鑫
Date:2021/11/26-18:10
==========================
"""
import time

'''
实列方法：最少需要包含一个self参数，用来绑定调用此方法的实列对象
类方法：用修饰器@classmethod 来表示其为类方法，对于类方法，第一个参数必须是类对象，一般以
cls作为第一个参数，推荐通过 类型.方法名 调用
静态方法：用修饰器@staticmethod 来表示其为静态方法，静态方法没有self/cls这样特殊参数，静态方法无法调用
任何类属性和方法

'''


class Emp:
    emp_no = ''
    emp_name = ''
    emp_sal = 2580

    # 计算年薪
    def year_sal(self):
        return self.emp_sal * 12

    # 计算请假天数扣款
    @classmethod
    def fine(cls, day):
        return cls.emp_sal / 22 * day

    @staticmethod
    def showtime():  # 静态方法没有self/cls这样的特殊参数，无法使用任何类型属性或类方法
        return time.strftime('%H:%M:%S', time.localtime())


# 实例方法：不能使用 类名.方法名 访问（必须通过实例对象去访问）
# Emp.year_sal()#TypeError: year_sal() missing 1 required positional argument: 'self'

emp01 = Emp()
emp01.emp_sal = 5000
print(emp01.year_sal())  # 60000

# 类方法：推荐 类名.方法名（）直接调用
print(Emp.fine(5))#586.3636363636364

#静态方法：推荐使用 类名.方法名（）直接调用
print(Emp.showtime())#18:23:35
