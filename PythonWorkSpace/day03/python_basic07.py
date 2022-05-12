"""
=========================
File Name:python_basic07.py
Author:冯鑫
Date:2021/11/17-9:57
==========================
"""
'''
本章讲解：列表 list
列表的定义：[]
列表的作用：可以存储任意类型的一组数据
列表属于序列之一
特点：有序，可变类型
'''
list1 = ['小花', '小兰', '小红', '小丽', [1, 2, 3], 100, 50, True]
print(list1)  # ['小花', '小兰', '小红', '小丽', [1, 2, 3], 100, 50, True]
# 知识点1：列表的下标
print(list1[0])  # 小花
print(list1[-1])  # True
print(list1[4])  # [1, 2, 3]
print(list1[4][0])  # 1  list1的4号位置是一个列表，这里找的是该列表的0号位置
print(list1[0][0])  # 小  list1的0号位置是一个字符串，这里找的是该字符的0号位置
# print(list1[5][1])#报错，数字类型是没有下标，不能通过下标访问TypeError: 'int' object is not subscriptable
print(id(list1))  # 2425068872328

# 知识点2：列表可以通过下标修改值
list1[1] = '小张'
print(list1)  # ['小花', '小张', '小红', '小丽', [1, 2, 3], 100, 50, True]
print(id(list1))  # 2330398253704

# 重新赋值，重新会指向新的地址，修改列表里面的数据，不会指向新的地址
list1 = [1, 2, 3]
print(id(list1))  # 2209313377096 重新赋值后，会重新指向一个新的物理地址

# 知识点3：切片，和字符串的切片是一样的
list1 = ['小花', '小兰', '小红', '小丽', [1, 2, 3], 100, 50, True]
print(list1[2:4])  # ['小红', '小丽']
print(list1[1:7:2])  # ['小兰', '小丽', 100]

# 知识点4：指定位置添加单个元素.insert(index,values)
list2 = ['a', 'b', 'c', 'd']
list2.insert(2, 'L')  # 在list2列表的第二个下标位置插入'L'，其他元素自动后移
print(list2)  # ['a', 'b', 'L', 'c', 'd']

# 知识点5:通过下标删除某个元素 .pop(index)
list2 = ['a', 'b', 'c', 'd']
list2.pop(2)  # 删除list2列表2号下标位置的元素
print(list2)  # ['a', 'b', 'd']

# 知识点6：清空所有元素.clear()
list2 = ['a', 'b', 'c', 'd']
list2.clear()  # 清空list2列表所有的元素
print(list2)  # 打印出来的是个空列表

# 知识点7：del完全删除对象：del在python中什么都能删 del  对象名：把对象从内存中删除
list2 = ['a', 'b', 'c', 'd']
del list2
# print(list2)#NameError: name 'list2' is not defined

# 知识点8；其他方法和函数
# 8.1 尾部添加多个元素.extend() 可以在尾部添加多个元素，合并成一个列表，只能在尾部添加
list3 = [1, 2, 3, 4, 5]
list3.extend([5, 6, 7])
print(list3)  # [1, 2, 3, 4, 5, 5, 6, 7]

# 8.2 在尾部添加多个元素.append()
list3 = [1, 2, 3, 4, 5]
list3.append(6)
print(list3)  # [1, 2, 3, 4, 5, 6]

# 8.3 根据元素的值进行数据删除.remove
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'a']
list3.remove('a')  # 删除元素'a',当list3里面存在多个元素’a‘的时候，删除首个’a‘
print(list3)  # ['b', 'c', 'd', 'e', 'f', 'a']

# 8.4 查找值对应的第一次出现的下标位置  .index
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'a']
res = list3.index('a')  # 在list3中查找元素'a'首次出现的位置
print(res)  # 0
# res2=list3.index('s')#ValueError: 's' is not in list

#8.5 统计元素在序列中出现的次数.count()
list3=['a', 'b', 'c', 'd', 'e', 'f', 'a']
res3=list3.count('a') #统计元素'a'在列表list3中出现了多少次
print(res3) #3

#8.6 求序列长度len()
list3=['a', 'b', 'b', 'd', 'a', 'f', 'a']
res4=len(list3)
print(res4)#7

#8.7 min() max() sum()  注意：除了数字以外，字母也有大小之分可以用min()和max(),但是不能用sun()
list4=[1,2,3,4]
print(min(list4))#1
print(max(list4))#4
print(sum(list4))#10

#知识点9：复制表 .copy()
list5=[1,2,3,4]
list6=list5.copy()
print(list6) #[1, 2, 3, 4]
print(id(list5),id(list6))#2163009424648 2163009424712

'''
注意复制和赋值的区别：.copy()是复制一个新的对象出来，赋值会让新变量也指向同一个对象
'''
a=[1,2,3,4]
b=a #赋值使用的是同一个对象
print(b)#[1, 2, 3, 4]
print(id(a),id(b))#2184999898824 2184999898824

c=a.copy()#复制是创建一个新的对象
print(id(c))#2558421143368

'''
如果a列表发生改变，b和c会跟着变化吗？
结论：a和b指向同一对象，所以a和b任意一个发生改变，另外一个都会跟着变
      c和a指向的不是同一个对象，所以无论a是否发生改变，c都不会改变
'''

a[0]=10#把a列表0号位置的元素修改为10
print(a)#[10, 2, 3, 4]
print(b)#[10, 2, 3, 4] b和a使用的同一对象，所以也跟着发生了改变
print(c)#[1, 2, 3, 4]  c使用的是一个独立对象，所有没有发生改变

'''
知识点：10 排序
'''
#10.1 升序排序，前提是列表里面一定是纯数字或者纯字母
list7=[5,100,34,550,1,7]
list7.sort()#进行升序排列，从小到大
print(list7) #[1, 5, 7, 34, 100, 550]

list8=[5,100,34,550,1,7,'a']
# list8.sort() #字母+数字进行排序会报错
print(list8)#TypeError: '<' not supported between instances of 'str' and 'int'

#10.2 降序排序
list9=[5,100,34,550,1,7]
list9.sort(reverse=True) #reverse=True 打开反转，一般反转开关是默认关闭，打开后排序规则变成从大到小
print(list9)#[550, 100, 34, 7, 5, 1]

#10.3 降序的第二种方式
list10=[5,100,34,550,1,7]
list10.sort() #先进行排序
print(list10) #[1, 5, 7, 34, 100, 550]
list10.reverse() #将已经排序好的列表list10倒过来

# 如果直接使用.reverse()
list11=[5,100,34,550,1,7]
list11.reverse()
print(list11)#[7, 1, 550, 34, 100, 5]

#知识点11：in/not in
# in 表示在.....里面（如果在指定序列里面找到指定的值那么返回True,反之返回False)
#not in  表示不在........里面（如果在指定序列里面没有找到指定的值那么返回True,反之返回False)

list12=[1,2,3,4]
bo1='a' in list12
print(bo1)#False
bo2='a' not in list12
print(bo2) #True

#知识点12：列表中的+和*的操作
list13=[1,2,3]
list14=['a','b','c']
print(list13+list14)#[1, 2, 3, 'a', 'b', 'c']
print(list13*5)#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]



