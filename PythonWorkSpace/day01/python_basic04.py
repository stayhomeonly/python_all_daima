"""
=========================
File Name:python_basic04.py
Author:冯鑫
Date:2021/11/15-16:12
==========================
"""
'''
本章讲解：数字类型、布尔类型
'''
# 1、常见的数字类型：int/float 整数/浮点数
a=10
b=10/3
print(a)  #10
print(b)  #3.3333333333333335

c=100.00
#查看变量的数据类型，用函数type()
print('变量a的类型是：',type(a)) #变量a的类型是：<class 'int'>
print('变量b的类型:',type(b)) #变量b的类型: <class 'float'>
print('变量c的类型:',type(c))#变量c的类型: <class 'float'>

#2、布尔类型(bool)：只有两个值True(真、成立)  False(假、不成立)
bo1=10<3
print(bo1)#False

bo2=10>3
print(bo2)#True

print('变量bo2的类型是:',type(bo2))#变量bo2的类型是: <class 'bool'>

#3、数字类型和布尔类型互相转
#(1)除了0以外，所有整数转换为bool类型，值都是True
#(2)除了0.0以外，所有浮点数转换为bool类型，值都是True

#bool()函数:可以强制将数据转换为bool类型
#int()函数：可以将数据强制转换为整数类型
#float()函数：可以将数据强制转换为浮点数类型
#str()函数：可以将数据强制转换为字符串类型
#注意：并不是一定能转换成功
"""
整数转换布尔类型
"""
c=1
bo3=bool(c) #将整数类型的c转换为bool类型，转换之后将值给bo3
print(bo3) #True
'''
浮点数转化布尔类型
'''
e=1.0
bo5=bool(e)  #将浮点数转换为bool类型
print(bo5)#True

f=0.0
bo6=bool(f)
print(bo6) #False

'''
布尔类型转换为浮点数或者整数
'''
bo7=True
bo8=False
print(int(bo7),int(bo8)) #当布尔类型转换为整数时，True和False分别转换为1和0，固定转换
print(float(bo7),float(bo8))#当布尔类型转换为浮点数时，True和False分别转换为1.0和0.0，固定转换

'''
总结：非0为真，非0为True
'''
#4、整数和浮点数互相转换，当浮点数转换为整数的时候会导致精度丢失
f=3.55 #f时浮点数类型
i=int(f)#将浮点数类型的f强制转换为整数类型
print(i) #3

#5、字符串在使用中的一些注意事项
#str是字符串类型，用来保存一串字符
#声明一个字符串类型变量的几种方式
str1='xiaohua'#声明了一个字符串
str2='''刘德华'''
str3="张三"
str4="""李小龙"""
print(str1)
print(str2)
print(str3)
print(str4)
print(type(str1))#<class 'str'>

#字符串中可以单引号和双引号配合使用
str5='我是一名优秀的"python"学员'
print(str5)#我是一名优秀的"python"学员 这里的双引号变成了字符串的一员

#字符串如果太长了可以使用反斜杠进行换行
str6='ffffffffffvsghhshhhdrhdjhdjdj' \
     'djdhsywysgsgsghshshshs' \
     'rhsrtthsgsgsbxkjdsxs'
print(str6)#如果字符串太长，可以在字符串中间按回车，python会自动修改格式，打印的结果任然是一行

#原样输出，按照书写的格式进行打印
str7="""君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。"""
print(str7) #取消编译，进行原样打印

# 5、input(),这个函数用来控制台输入，可以接收控制台输入的内容，并且保存到变量中（所有从控制台输入的内容都是字符串类型的）

name=input('请输入你觉得全亚洲最帅的男性的姓名:')
print('从控制台输入的姓名',name)
print(type(name)) #<class 'str'> 所有从控制台输入的内容都是字符串类型的，要按回车

#设计一个简单的计算器
num1=input("输入第一个数:")
num2=input("输入第二个数:")
print(num1+num2) #1213 注意所有从控制台输入的内容都是字符串格式的，字符串相加会进行拼接
print(int(num1)+int(num2)) #25,先将控制台输入的字符串强制转换为整数再进行计算