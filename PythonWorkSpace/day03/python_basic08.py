"""
=========================
File Name:python_basic08
Author:冯鑫
Date:2021/11/17-19:47
==========================
"""
'''
本章讲解：元组 tuple，有序
元组的定义：用()存储一组数据，为不可变类型，创建后不能修改数据
           任意对象用逗号分隔都默认为元组
           创建元组的主要符号是 逗号 ，
           元组也是序列之一
           （三大序列：str字符串/list列表/tuple元组）
'''

#知识点1：元组的创建
tup1=('xiaohua','xiaobai',1,2,[40,50,60],(77,88,99))
print(tup1)#('xiaohua', 'xiaobai', 1, 2, [40, 50, 60], (77, 88, 99))
print(type(tup1))#<class 'tuple'>

tup2=1,2,3,4
print(tup2)#(1, 2, 3, 4)
print(type(tup2))#<class 'tuple'>

tup3=1,
print(tup3)#(1,)
print(type(tup3))#<class 'tuple'>
#如果元组里面只有一个元素，那么必须在元素后面加逗号
tup4=(1)#这里声明的不是元组，这是一个int类型
print(type(tup4))#<class 'int'>

tup4=(1,)#这里声明一个元组
print(type(tup4))#<class 'tuple'>

#知识点2：通过下标查看元组中的数据
tup5=('xiaohua','xiaobai',1,2,[40,50,('a','b','c'),60],(77,88,99))
print(tup5[2])#1
print(tup5[4][1]) #50
print(tup5[4][2][1])#b
#print(tup5[100]) #不存在下标11，报错：IndexError: tuple index out of range

#知识点3：元组切片，所有的序列切片都是一样的
tup6=('小花','小兰','小红','小丽',[1,2,3],100,50,True)
print(tup6[1:4])#('小兰', '小红', '小丽')
print(tup6[3:])#('小丽', [1, 2, 3], 100, 50, True)
print(tup6[1:7:2])#('小兰', '小丽', 100)

#知识点4：统计元组中元素出现的次数 .count()
tup7=('a','b','c','d','e','f','a')
res1=tup7.count('a') #统计元素'a'在元组中出现了多少次
print(res1)#2

#知识点5:查找元素下标位置.index()
tup8=('a','b','c','d','e','f','a')
res2=tup8.index('e') # 查找元素’e‘在元组中第一次出现的位置
print(res2)#4

#知识点6：元组不能修改，但是可以拼接
tup9=('小花','小兰','小红','小丽',[1,2,3],100,50,True)
#tup9[2]='小白' #元组无法通过下标去修改，会报错TypeError: 'tuple' object does not support item assignment
#print(tup9)

tup10=(1,2,3)
tup11=('a','b','c')
tup12=tup10+tup11  #拼接后变成新的元组
print(tup12)#(1, 2, 3, 'a', 'b', 'c')

print(id(tup12))#2112464022984

tup13=tup12
print(id(tup13))#2112464022984

#知识点7：元组中的可变类型可以修改
tup14=('小花','小兰','小红','小丽',[1,2,3],100,50,True)
print('这是修改前的地址',id(tup14))#这是修改前的地址 2634777481736
tup14[4][0]=77
print(tup14)#('小花', '小兰', '小红', '小丽', [77, 2, 3], 100, 50, True)

print('这是修改后的地址',id(tup14))#这是修改后的地址 1785642013192

#元组里面的可变类型被修改后地址是否发生改变：不会

#知识点8：元组和其他序列一样可以使用 +/*/len/in/not in/ max()/min()/sum()....
'''
可变类型：列表
不可变类型：数字，字符串，元组
'''
str1='aadasdsa'
print(str1[1]) #a
#str1[1]='b'
#print(str1)#TypeError: 'str' object does not support item assignment




