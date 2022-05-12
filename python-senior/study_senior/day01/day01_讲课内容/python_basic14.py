"""
-----------------------------
 Time    : 2021/9/2 16:58
 Author  : Lee
 File    : python_basic34.py
-----------------------------
"""

"""
本章讲解:数字类型、布尔类型、字符串类型
"""

# 数字类型  分为 int / float
a = 10
b = 10 / 3

print(a)  # 10
print(b)  # 3.3333333333333335

# 查看类型的函数 type()
print('a的变量类型为:', type(a))  # a的变量类型为: <class 'int'>
print('b的变量类型为:', type(b))  # b的变量类型为: <class 'float'>

# 布尔类型(bool):只有2个值，  True(真、成立)  False(假、不成立)
bo1 = 10 < 3
print(bo1)  # False

bo2 = 10 > 3
print(bo2)  # True
print('变量bo2的类型为:', type(bo2))  # 变量bo2的类型为: <class 'bool'>

# 字符串:用来保存一串字符  str
str1 = 'xiaohua'
str2 = '''xiaomei'''
str3 = "xiaozi"
str4 = """xiaolan"""

print(str1, str2, str3, str4)  # xiaohua xiaomei xiaozi xiaolan

# 字符串在使用过程中的一些注意事项
# 1.单引号和双引号可以配合使用，但是需要符合书写规范
print("李洁洁是个'优秀'的测试工程师!")  # 李洁洁是个'优秀'的测试工程师! 单引号变成了字符串里的成员
print("my name's China!")  # 点名提问打印结果

# 类型转换, 使用  类型() 进行类型转换
# 1、数字类型的字符串 和 数字之间转换

strs = str(100)
print(strs, type(strs))  # type()用来查看  <class 'str'>

nums = int("100")
print(nums, type(nums))

# 2、布尔类型和数字转换,布尔类型
print(int(True))  # 1
print(int(False))  # 0

# 非0为true
print(bool(1))
print(bool(-1))
print(bool(0))

# 其他类型转布尔类型
print(bool('abc'))  # True
print(bool(''))  # False
print(bool(None))  # False
