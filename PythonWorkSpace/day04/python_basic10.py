"""
=========================
File Name:python_basic10
Author:冯鑫
Date:2021/11/18-14:28
==========================
"""
'''
本章讲解：字典以key-value形式来保存{key1:value1,key2:value2,key3:value3,key4:value4.....}
          字典是可变类型
          特点：无序，且key(键)不可重复，key(键)必须是不可变类型，但是值可以重复
'''

# 知识点1：字典的定义
dict1 = {"username": "xiaohua1", "password": "a123456", "re_password": "a123456", "phone": "15912341235", "sex": "女"}
print(
    dict1)  # {'username': 'xiaohua1', 'password': 'a123456', 're_password': 'a123456', 'phone': '15912341235', 'sex': '女'}
print(type(dict1))  # <class 'dict'>

# 知识点2：通过key值获取value
dict1 = {"username": "xiaohua1", "password": "a123456", "re_password": "a123456", "phone": "15912341235", "sex": "女"}
# 方法1:
print(dict1["username"])  # xiaohua1
# 方法2：
print(dict1.get('username'))  # xiaohua1

# 知识点3：给字典增加一个key-value(键值对)
dict2 = {"username": "xiaohua1", "password": "a123456", "phone": "15912341235", "sex": "女"}
dict2['loc'] = 'shanghai'  # 给dict2增加一个键值对‘loc’:'shanghai'
print(dict2)  # {'username': 'xiaohua1', 'password': 'a123456', 'phone': '15912341235', 'sex': '女', 'loc': 'shanghai'}

# 知识点4：给字典增加多个键值对 .update 注意增加后，字典对应的地址不会发生改变
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
print(id(dict3))  # 2112842334000
dict3.update({'phone': '15912341235', 'loc': 'shanghai'})
print(dict3)  # {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}
print(id(dict3))  # 1803573034872

# 知识点5：通过key值去修改value值
dict4 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}
dict4['age'] = 19  # 将字典dict4中的‘age’重新赋值19
print(dict4)  # {'name': 'xiaohua', 'age': 19, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}

# 知识点6：根据key,删除key-value  .pop
dict5 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}
dict5.pop('name')  # 将dict5字典中‘name’对应的key-value进行删除
print(dict5)  # {'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}

# 知识点7：清空字典
dict6 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}
dict6.clear()
print(dict6)  # {}

# 知识点8：获取字典中的key使用，获取字典中的所有value
dict7 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai'}

# 8.1 获取key值使用 .keys()
ks = dict7.keys()
print(ks)  # dict_keys(['name', 'age', 'sex', 'phone', 'loc'])

# 8.2 获取value使用 .values()
vs = dict7.values()
print(vs)  # dict_values(['xiaohua', 18, '女', '15912341235', 'shanghai'])
print(type(ks), type(vs))  # <class 'dict_keys'> <class 'dict_values'>

# 8.3 获取所有的key-value
kvs = dict7.items()
print(
    kvs)  # dict_items([('name', 'xiaohua'), ('age', 18), ('sex', '女'), ('phone', '15912341235'), ('loc', 'shanghai')])

# 获取的key数据和value数据都可以直接转换为列表、元组、集合
print(list(ks))  # ['name', 'age', 'sex', 'phone', 'loc']
print(list(vs))  # ['xiaohua', 18, '女', '15912341235', 'shanghai']
print(tuple(ks))  # ('name', 'age', 'sex', 'phone', 'loc')
print(set(ks))  # {'phone', 'age', 'sex', 'name', 'loc'}

# 求出所有的value,并且过滤掉重复的值，再转换为列表
dict8 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'phone': '15912341235', 'loc': 'shanghai', 'nickname': 'xiaohua'}
vs = dict8.values()
print(vs)  # dict_values(['xiaohua', 18, '女', '15912341235', 'shanghai', 'xiaohua'])
set5 = set(vs)
print(set5)  # {'shanghai', 18, '女', 'xiaohua', '15912341235'}
list2 = list(set5)
print(list2)  # ['shanghai', 18, '女', 'xiaohua', '15912341235']

# round 函数：保留指定的小数位

a = 15.3
b = 3
c = a / b
print(round(c, 1))
print(round(3.12344, 2))
