"""
# @Time : 2022/5/2 15:43
# @File : python_basic36
# @Project : python_0406
# @Content :
"""
"""
各数据类型共同特征和不同特征
1、从保存值得方式来看，列表、元组、字典、集合都可以保存一组数据
2、列表和元组是可以通过下标去访问的，但是集合和字典没有下标，字典可以通过key获取value
3、增删改方式不同
可变类型：列表，集合，字典         (值可以改变)
不可变类型：数字，字符串，元组      (值不能发送改变)

"""
# 1、从保存值得方式来看，列表、元组、字典都可以保存一组数据
# 保存一组双色球
list1 = [1, 7, 12, 14, 15, 28, 10]
tuple1 = (1, 7, 12, 14, 15, 28, 10)
set1 = {1, 7, 12, 14, 15, 28, 10}
dict1 = {"第一个球": 1, "第二个球": 7, "第三个球": 12, "第四个球": 14, "第五个球": 15, "第六个球": 28, "第七个球": 10}

# 2、列表和元组是可以通过下标去访问的，但是集合和字典没有下标，字典可以通过key获取value
print(list1[3])  # 14
print(tuple1[2])  # 12
# print(set1[4])  # 集合无法下标访问
print(dict1["第三个球"])  # 12  字典不能通过下标访问，但是可以通过key获取value    .get(key)

# 3、增删改方式不同
# (1)各类型的新增方式
# 列表
list1.append("a")  # 列表增加元素用  append
print(list1)
# 元组
print("元组为不可变类型，不能进行增删改")
# 集合
set1.add("a")  # 集合增加元素用 add
print(set1)
# 字典
dict1["第八个球"] = 666  # 字典增加直接使用self[key] = value  这个key是原字典不存在的
print(dict1)

# (2) 各类型的删除方式
# 列表
list1.pop(1)  # 列表通过下标删除使用 pop()
list1.remove(10)  # 列表直接删除对应的元素 10，删除的是第一个匹配项
# 元组
print("元组为不可变类型，不能进行增删改")
# 集合
set1.remove(15)  # 集合直接通过值进行删除
# 字典
dict1.pop("第八个球")  # 字典通过key进行删除

# (3) 各数据类型，修改元素
# 列表
list1[0] = 777  # 列表类型可以直接通过下标进行修改
print(list1)  # [777, 12, 14, 15, 28, 'a']
# 元组和集合
print("元组为不可变类型，不能进行增删改")
print("集合没有下标，所以没办法直接修改值")
# 字典
dict1["第一个球"] = 777  # 直接通过key修改value
print(dict1)  # {'第一个球': 777, '第二个球': 7, '第三个球': 12, '第四个球': 14, '第五个球': 15, '第六个球': 28, '第七个球': 10}

# 以上这些就是关于列表、元组、字典、集合的增删改总结

# 4、列表、元组、字典、集合的其它公共API
list1 = [1, 7, 12, 14, 15, 28, 10]
tuple1 = (1, 7, 12, 14, 15, 28, 10)
set1 = {1, 7, 12, 14, 15, 28, 10}
dict1 = {"第一个球": 1, "第二个球": 7, "第三个球": 12, "第四个球": 14, "第五个球": 15, "第六个球": 28, "第七个球": 10}

# (1) 切片：有下标的数据类型(字符串、列表、元组)可以通过切片获取一部分的值
# 字符串切片
str1 = "abcdefg"
print(str1[0:5])  # abcde  截取0号位置开始，在5号位置之前结束，前包含，后不包含
print(str1[1:4])  # bcd    截取1号位置开始，到4号位置之前结束，不包含4号位置
print(str1[-5:-2])  # cde  注意：下标位置从后往前从-1 开始   a(-7)b(-6)c(-5)d(-4)e(-3)f(-2)g(-1)
# 元组和列表进行切片
print(list1[1:6])  # [7, 12, 14, 15, 28]
print(tuple1[1:-2])  # (7, 12, 14, 15)
print(list1[:6])  # [1, 7, 12, 14, 15, 28]  前下标为空时，从第一个数据开始截取
print(list1[3:])  # [14, 15, 28, 10]  当后下标为空时，截取3号位后所有数据

# （2） 求长度使用len()
print(len(list1), len(tuple1), len(set1), len(dict1))

# (3) 判断某个元素是否存在于 列表、元组、集合、字典中  使用  in   \  not  in
print(7 in list1)  # True  7在list1里面，给出结果为True
print(7 not in list1)  # False   表达不成立给出结果为 False
print("第一个球" in dict1)  # True  字典是判断值是否存在于KEY里面
print(1 in dict1)  # False  这个表达式判断 1这值是否存在于 dict1的key里面
# 如果我需要判断这个1在不在字典的value里面
print(1 in dict1.values())  # True 这个表达式判断1是否存在于字典的value里面 ，先通过dict1.values()获取所有的value，再进行判断

# （4）求列表、元组、集合、字典中：最大值max()  /  最小值min()  / 求和sum()  需要我们所有的元素都是数字类型
print("列表list1的最大值为：{}，最小值为：{},和为{}".format(max(list1), min(list1), sum(list1)))
print("元组tuple1的最大值为：{}，最小值为：{},和为{}".format(max(tuple1), min(tuple1), sum(tuple1)))
print("集合set1的最大值为：{}，最小值为：{},和为{}".format(max(set1), min(set1), sum(set1)))
# 要求字典最大值、最小值、和需要先将字典的value拿出来
values = dict1.values()
print(values)  # dict_values([1, 7, 12, 14, 15, 28, 10])
print("字典dict1的最大值为：{}，最小值为：{},和为{}".format(max(values), min(values), sum(values)))

# (5)字符串、列表、元组中，统计元素出现次数使用count()
str1 = "i am a teacher"
print(str1.count('a'))  # 3  这里返回的是a这个元素在字符串str1里面出现的次数

list2 = ["a", "b", "a", "d", "e", "b", "c"]
print(list2.count("b"))  # 2

tup2 = ("a", "b", "a", "d", "e", "b", "c")
print(tup2.count("a"))  # 2

str12 = '1234456'
str13 = str12.split(' ')
print(str13, type(str13))


