"""
# @Time : 2022/5/2 15:19
# @File : python_basic35
# @Project : python_0406
# @Content :
"""
"""
字典：以key(键) - value(值) 形式来保存数据{key1:value1,key2:value2,key3:value3.....}

"""

# 1、字典的定义
dict1 = {}  # 定义一个空字典
dict2 = {"name": "xiaohua", "age": 18, "sex": "nv"}

# 2、使用key获取value
print("name键对应的值为", dict2["name"])  # name键对应的值为 xiaohua

# 3、通过key值获取value，方式2   .get()
print("name键对应的值为", dict2.get("name"))  # name键对应的值为 xiaohua

# 4、通过key值修改value
dict2["name"] = "xiaobai"
print("字典修改name后", dict2)  # {'name': 'xiaobai', 'age': 18, 'sex': 'nv'}

# 5、根据key值删除value,删除性别
dict2.pop("sex")
print("删除后的字典", dict2)  # {'name': 'xiaohuahua', 'age': 18}

# 6、给字典增加一个键值对
dict2["tel"] = 15877773333
print("增加tel键值后的字典", dict2)  # 增加tel键值后的字典 {'name': 'xiaohuahua', 'age': 18, 'tel': 15877773333}
# 操作的key存在的，那么进行的是修改，如果key不存在，那么进行的是新增

# 7 ，其他知识
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': 'nv', 'tel': 15877773333}

# 获取所有的key使用 .keys()
ks = dict3.keys()
print(ks)  # dict_keys(['name', 'age', 'sex', 'tel'])

# 获取所有的value使用 .values
vs = dict3.values()
print(vs)  # dict_values(['xiaohua', 18, 'nv', 15877773333])

# 获取所有的键值对使用items()
kvs = dict3.items()
print(kvs)  # dict_items([('name', 'xiaohua'), ('age', 18), ('sex', 'nv'), ('tel', 15877773333)])

# key不能重复的，如果一个字典里面声明了两个相同的key，以后面声明的那个为准
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': 'nv', 'tel': 15877773333, "name": "xiaobao"}
print(dict3)  # {'name': 'xiaobao', 'age': 18, 'sex': 'nv', 'tel': 15877773333}
