"""
=========================
File Name:python_basic05.py
Author:冯鑫
Date:2021/11/16-10:24
==========================
"""
# 知识点1：声明一个字符串类型变量的几种方式
str1 = 'xiaohua'  # 声明了一个字符串
str2 = '''刘德华'''
str3 = "张三"
str4 = """李小龙"""

# 知识点2：字符串和数字可以互相转换，但是字符串转数字必须保证被转的值是数字类型
# 2.1 数字转字符串
age = 18
print(type(age))  # <class 'int'>
age = str(age)
print(type(age))  # <class 'str'>

# 2.2 字符串转化为数字（字符串转数字必须保证被转的值是数字类型）
name = 'xiaohua'
print(type(name))  # <class 'str'>
# name=int(name) #字符串'xiaohua'不是数值，无法转换为数字，ValueError: invalid literal for int() with base 10: 'xiaohua'

tel = '15161039042'
print(type(tel))  # <class 'str'>
tel = int(tel)  # 这个转换没有换错，因为tel里面装的数值
print(type(tel))  # <class 'int'>

# 2.3字符串转换为布尔类型
name = 'xiaohua'
bo1 = bool(name)
print(bo1)  # True

name1 = ''  # 这个声明了一个字符串类型的空值
bo2 = bool(name1)
print(bo2)  # False

'''
数字转字符：可以直接转，基本不受限制
字符转数字：需要被转化的字符串必须是纯数字
数字转布尔：非0为True
布尔转数字：True为1，False为0
字符转布尔:非空为True
'''

# 知识3：字符串使用+号拼接，结果还是一个字符串
str1 = '今天'
str2 = '天气'
str3 = '很舒适'
str4 = '好想学python'
str5 = str1 + str2 + str3 + str4
print(str5)  # 今天天气很舒适好想学python

# 3.1 字符串不能和数字进行加、减、除的操作
name = 'xiaohua'
age = 18
# print(name+age) TypeError:数字和字符串类型不能相加

# 3.2 字符串可以和整数进行乘法操作
a = 'xiaohua'
print(a * 10)  # xiaohuaxiaohuaxiaohuaxiaohuaxiaohuaxiaohuaxiaohuaxiaohuaxiaohuaxiaohua
'''
知识点4；字符串的索引，字符串对每个字符都做了编号（下标），从前往后从0开始，从后往前是从-1开始
'''

str6 = '学python使我快乐'  # 总计是11个字符组成了一个字符串

print(str6[0])  # 学 在0号位置 【】这个里面的数字代表位置
print(str6[5])  # o
print(str6[-1])  # 乐
print(str6[-5])  # n
# print(str6[100])获取字符串里面不存在的下标时，会报错；IndexError: string index out of range

# length:长度，len()函数可以求字符串的长度
print(len(str6))  # 11
# 题目：如果我要获取一个字符串的最后一位，除了用str6[-1]
# 另外一种写法：print(str6[len(str6)-1])

# 特殊切片
str7 = 'abcdefghijkl'  # 位置下标0-11

print(str7[1:5])  # bcde 就是从下标1到下标5，不包含5
print(str7[1:5:2])  # bd 2是步长
print(str7[1:9])  # bcdefghi
print(str7[1:9:2])  # bdfh 先截取了str7字符串的1-9位下标的字符，不包含位9的字符，步长为2
print(str7[1:9:3])  # beh 先截取了str7字符串的1-9下标的字符，不包含位9的字符，步长为3
print(str7[::2])  # acegik
print('*' * 100)
print(str7[::-1])  # lkjihgfedcba 倒叙打印字符串
# 知识点6：字符串的转义 \n换行符  \t制表符 相当于一个tab
str8 = 'py\tho\ncccc'
print(str8)
# 关闭转义：可以在字符串前面加r/R,关闭转义
str8 = r'py\tho\ncccc'
print(str8)  # 关闭转义，原样输出
str9 = r'fagagga\taafgag\nfafaf\t'

# 知识点7：字符串常用的函数
# length:长度，len()函数可以求字符串的长度
print(len(str6))  # 11
# 题目：如果我要获取一个字符串的最后一位，除了用str6[-1]
# 另外一种写法：print(str6[len(str6)-1])

# 7.2 count()统计元素在字符串中出现的次数，返回是一个int
str10 = 'aabbccddajs'
res1 = str10.count('a')
print(res1)  # 3 'a'在字符串str10中出现了3次
res2 = str10.count('aa')
print(res2)  # 1

# 7.3 find()方法，查找括号中元素在字符串中第一次出现的下标位置，返回是一个int
str10 = 'aabbccddajs'
res3 = str10.find('c')
print(res3)  # 4 元素‘c’在字符中第一出现的位置是4号位置

# 7.4 replace(a,b)方法，可以将字符串中的a元素替换成b元素，替换后会返回替换完成的数据
str10 = '你喜欢小花'
str11 = str10.replace('小花', '小红')
print(str11)  # 你喜欢小红
str11 = str10.replace('喜欢', '特别特别喜欢')
print(str11)  # 你特别特别喜欢小花

# 7.5 isnumeric()判断函数，判断字符串里面的元素是不是纯数值，如果是就返回True 否则返回False
age = '123456'
print(age.isnumeric())  # True

name = 'a123456'
print(name.isnumeric())  # False

'''
知识点8；填充
'''
# 8.1 format()
str12 = '小花来自于{},今年{},{}来上海工作'
str13 = str12.format('安徽', 18, '2021年10月15')  # 填充的值的数量要和{}数量对应
print(str13)  # 小花来自于安徽,今年18,2021年10月15来上海工作

print('小花每天上班{}小时,月薪{}元,加班费{}元'.format(15, 3000, 20000))  # 小花每天上班15小时,月薪3000元,加班费20000元

# 8.2 传统填充方式 %s代表字符串类型的数据  %d代表int类型的数据 %f 代表浮点数数据，默认保留6位，这些叫占位符
str14 = '小花来自于%s,今年%d岁,目前年收入%f万元'
str15 = str14 % ('安徽', 18, 15.555555)
print(str15)  # 小花来自于安徽,今年18岁,目前年收入15.555555万元
print('小白全名叫%s,今年%d岁,身高%f' % ('江小白', 25, 1.88))  # 小白全名叫江小白,今年25岁,身高1.880000
# 求出a中的哪个字母出现的次数最多
a = 'kakgjgngkgjgjigijejiawpqplcmvnbnb'
b = {}
for i in a:
    b[i] = a.count(i)
for i in b.keys():
    if b[i] == max(list(b.values())):
        print(i)

# 另外一个写法,分别写出所有的字符出现的次数
from collections import Counter

print(dict(Counter(a)))

# 哪个字符出现的次数最多
print(max(a, key=a.count))
