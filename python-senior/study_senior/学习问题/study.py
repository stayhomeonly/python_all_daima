"""
#@Time：2022/5/1-23:51
#@file：study
#@Project:python-senior
#@Content:

"""
codes = [(1000, '北京'),
         (1100, '天津')]

codes_dict = {code: city
              for code, city in codes}

print(codes_dict)
# 把列表里面的偶数去掉
# 第一种最常见的办法
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_list = []
# for i in range(len(original_list)):
#     if original_list[i] % 2 == 1:
#         new_list.append(original_list[i])
#
# print(new_list)
# original_list = new_list
# print(original_list)

# 根据下标删除法
i = 0
while i < len(original_list):
    if original_list[i] % 2 == 0:
        original_list.remove(original_list[i])  # 注意用remove删除的时候只能删除当前下标，然后删除之后
        # 后面的一位就会向前位移，然后代码默认已经操作过了，所以下标要向前一位，重新来过
        i = i - 1
    i = i + 1
print(original_list)

#  第二种方法
# new_list = filter(lambda x:
#                   False if x % 2 == 0
#                   else True
#                   , original_list)  # filter 筛选出符合条件的数据  lambda 用于定于函数
# print(new_list)

# 第三种办法
# new_list = [i
#             for i in original_list
#             if i % 2 != 0]
# print(new_list)


# def jishu(number_list):
#     new_list = [i
#                 for i in number_list
#                 if i % 2 != 0]
#     return new_list
#
#
# print(jishu(original_list))

# 元组组包
tuple1 = ('name', 'age', 'sex')
tuple2 = ('fengxin', '18', 'nan')
list1 = ['name', 'age', 'sex']
list2 = ['fengxin', '18', 'nan']
dict2 = dict(zip(tuple1, tuple2))
dict3 = dict(zip(list1, list2))
print(dict2, dict3)

# 拆包
str1 = '12345'
a, b, c, d, e = str1
print(str1)
# 列表拆包
my_lsit = [1, 3.14, 'hello', True]
num, pi, my_str, my_bool = my_lsit
print(num, pi, my_str, my_bool)

# 字典拆包
my_dict = {"name": "老王", "age": 19}
ret1, ret2 = my_dict
print(ret1, ret2)
# 字典拆包的区别在于赋值的只是key


list12 = [1, 2, 3, 4, 5, 5, 6, 7]
print(list12[3:])  # [4, 5, 5, 6, 7],从第三位开始到最后一位，最后一位也包含
