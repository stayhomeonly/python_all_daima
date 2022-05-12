"""
=========================
File Name:python_basic06.py
Author:冯鑫
Date:2021/11/16-19:09
==========================
"""
'''
本章讲解：运算符

'''
# 知识点1：算数运算符 + - * / %(取余) //(向下取整)  **(冥数)
print(10 + 20)  # 30
print(20 - 10)  # 10
print(20 * 10)  # 200
print(20 / 10)  # 2.0 为了更加精确，python在进行除法计算是，会自动将结果转换为浮点数
print(10 / 3)  # 3.3333333333333335
print(7 % 3)  # 1
print(2 ** 3)  # 8
print(-7 // 3)  # -3

# 所有奇数对2取余都是1，所有偶数对2取余结果都是0，所有的小对大取余结果都是取小
print(1 % 2)  # 1
print(3 % 2)  # 1
print(5 % 2)  # 1
print(7 % 2)  # 1

print(2 % 2)  # 0
print(4 % 2)  # 0

print(2 % 5)  # 2
print(7 % 8)  # 7

# 知识点2：赋值运算符  = +=  -=  /=  *=  //=  %=  **=
a = 10
a += 1  # 相当于a = a + 1
print(a)  # 11

a -= 1  # 相当于a=a-1
print(a)  # 10

a *= 2  # 相当于a=a*2
print(a)  # 20

a /= 2  # 相当于a=a/2
print(a)  # 10.0

a //= 3  # 相当于a//3
print(a)  # 因为45行代码进行除法运算，a变成了浮点数类型，注意：浮点数和整数进行任何运算结果都是浮点数

a = 10  # 重新给a赋值为整数
a %= 4  # 相当于a=a%4
print(a)  # 2

a **= 3  # 相当于a=a**3
print(a)  # 8
# 知识点3：比较运算符 > < <=  >= !=(不等于） ==(相等），结果是布尔类型，只能是True和False
a = 10
b = 20
c = 20
print(a > b)  # False
print(a < b)  # True
print(a == b)  # False
print(b >= c)  # True
print(a <= b)  # True

# 知识点4：逻辑运算符号 and(全真为真) or(全假为假)
# and(全真为真) (条件A and 条件B) 只有这两个条件同时成立的时候，最终结果为True
# or(全假为假) (条件A or 条件B) 只有这两个条件都不成立的时候，最终的结果为False

a = 10
b = 20
c = 20

print(a > 0 and b > 0)  # True
print(a < 0 and b > 0)  # False
print(a < 0 or b > 0)  # True
print(a < 0 or b < 0)  # False
print(a > 0 and (a < 0 or b > 0))  # True


# 知识点5：not 取反，反义  not True 就是False  not False 就是True
bo1 = 10 < 20
print(bo1)  # True
print(not bo1)  # False
print(not (10 > 20))  # True

# 知识点6：成员运算符 in 和not in
# in 表示在.......里面(如果在指定序列里面找到指定的值那么返回True，反之返回False
# not in 表示不在.......里面(如果在指定的序列里面没有找到指定的值那么返回True,反之返回False)
str1 = 'abcd'
print('a' in str1)  # True
print('a' not in str1)  # False
print('s' not in str1)  # True

'''
查看物理存储地址函数 id()
'''

a=100
print(id(a)) #140722243952768
b='xiaohua'
print(id(b)) #3061413515928
c=100
print(id(c)) #140722243952768

#知识点7：身份运算符 is 判断两个标识符(变量)是否为同一对象，比较存储地址，如果是同一地址就返回True,否则返回False
  #is not 判断两个标识符（变量）是否为同一对象，比较储存地址，如果是同一地址就返回False,否则返回True

a=10
b=10
print(id(a),id(b)) #140722243949888 140722243949888
print(a is b) #True

c='xiaohua'
d='xiaohua'
print(id(c),id(d))#2329494491800 2329494491800
print(c is not d)#False

a=10
b=10.0
print(id(a),id(b))#140722243949888 2245698433432
print(a is b) #False

'''
is 和== 区别是什么，is用来判断两个变量是否引用的同一物理地址，==用来判断变量的值是否相等
'''

'''
小整数池：-5到256，是由python解释器规定的
大整数池：对小整数池的扩容，将一些比较简单的数据类型放入到大整数池，代码运行结束，才进行清除，由pycharm进行扩容
'''

a=256
b='xiaohua'
c='xiaohua'
print(id(a))#140722243957760
print(id(b))#2600591364760
print(id(c))#2600591364760

e=[1,2,3]
f=[1,2,3]
print(id(e),id(f))#2737783923272 2737783923336

#小整数池数据创建一次，在整个空间内都能使用
#大整数池数据在一个python文件里面只会创建一次
#其他数据，每次声明都会占用一个新的地址