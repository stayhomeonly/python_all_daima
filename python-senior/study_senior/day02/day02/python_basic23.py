"""
# @Time : 2022/4/23 11:05
# @File : python_basic21
# @Project : python_0406
# @Content : 字符串相关 API
"""
# 1、len() 求字符串长度  length的缩写(长度)
name = "小花"
print(len(name))  # 2

# 字符串长度 和 最大下标 的关系  最大长度-1 == 最大下标
# print(name[2])  # IndexError: string index out of range 下标越界错误

# 2、字符串内容的替换   str.replace(a,b) 会把 str 中的 a 替换成b
str1 = "疫情很快会过去的！"
str2 = str1.replace("的", "吧")
print(str2)  # 疫情很快会过去吧！

# 练习：去除字符串中所有的空格 "abcdef g h i j kht"

str3 = "abcdef g h i j kht"
str4 = str3.replace(" ", "")
print(str4)

# 字符串 find() 查找字符串中 元素第一次出现的次数
str5 = "i like python"
index = str5.find('i')
print(index)  # 0
index = str5.find('C')
print(index)  # -1

# join 拼接
str6 = "|".join("12345")
print(str6)  # 1|2|3|4|5

# count 统计元素在字符串中出现的次数

str7 = "i like python"
print(str7.count("i"))  # 2
print(str7.count("py"))  # 1
print(str7.count("C"))  # 0  不存在结果为 0

# upper将字符串转为大写/lower 将字符串转为小写
print("I Like Python".upper())  # I LIKE PYTHON
print("I Like Python".lower())  # i like python

# isnumberic() 判断字符串是否为数字类型的字符串，如果是返回True 反之返回 False
print("12345".isnumeric())  # True
print("1234a".isnumeric())  # False

# 案例:
a = input("请输入第一个数:")
b = input("请输入第二个数:")
if a.isnumeric() and b.isnumeric():
    c = int(a) + int(b)
    print(a + "+" + b + "=" + str(c))
else:
    print("请输入数字！")

# 切分字符串,字符串可以进行切分，切分后返回列表

lst1 = "2018-10-20".split("-")
print(lst1)  # ['2018', '10', '20']
# 获取当前时间中的分钟数
lst2 = "15:11:00".split(":")
print(lst2)  # ['15', '11', '00']
print(lst2[1])  # 获取列表下标为 1 位置的值

lst3 = "12  34 5".split()
print(lst3)  # ['12', '34', '5']
print(''.join("12 34 5".split()))  # 12345

# 1、 把列表转为字符串 [1,2,3,4,5] 转换为 12345
lst4 = [1, 2, 3, 4, 5]
str5 = str(lst4).replace(',', '')
print(str5)
str6 = str5.replace(' ', '')
print(str6, type(str6))
