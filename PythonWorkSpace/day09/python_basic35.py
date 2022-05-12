"""
=========================
File Name:python_basic35
Author:冯鑫
Date:2021/11/26-11:50
==========================
"""

'''
知识点1：面向对象：面向对象是一个编程思想（一切皆对象）
知识点2：类和对象
       类：具有相同特征的一类事物的描述
       比如订单,所有订单类都应该有以下的功能：
            静态的内容：商品编号、商品价格、商品数量、商品信息..........
            动态的内容：加入商品、删除商品、修改数量..............
        
        对象：对象是类的一个具体实列（比如：小王的订单、小李的订单）
        
        对象和类的关系：一个类可以有无数个对象
知识点3：类的构成
        类中包含属性和方法
        属性：把静态的内容抽象出来,并且用变量进行声明(类中的变量就是属性）
        方法：把动态的内容抽象出来，并且函数进行声明（类中的方法就是函数）
知识点4：self 代表当前对象

'''


# 创建一个类
class Cat:  # 类的名字首字母必须大写
    color = ''
    name = ''
    sex = ''

    def eat(self, food):
        print('{}很好吃'.format(food))

    def run(self):
        print('小样来追我呀')


# 创建实列对象
cat1 = Cat()
cat2 = Cat()

#为对象属性赋值
cat1.color='白色'
cat1.sex='母'


# 对象可以调用类的方法
cat1.eat('杰瑞')
cat1.run()

cat1.eat('面条')

# 定义一个类,并且声明属性和方法,创建该类的对象,并且为对象的属性赋值,再调用该对象的方法


class Computer:
    style = ''
    color = ''
    size = ''

    def type(self, type):
        print('{}真好用'.format(type))

    def agility(self):
        print('非常好')


# 创建实列对象
cp2 = Computer()
cp3 = Computer()

# 给对象的属性赋值
cp2.color = '黑色'
cp2.size = '非常合理'
# 调用类的方法
cp3.type('笔记本')
cp3.agility()


list1=[1,4,3,6,7,2,0]

for i in range(len(list1)-1):
    for j in range(len(list1)-1-i) :
        if int(list1[j])>int(list1[j+1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()






