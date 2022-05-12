"""
=========================
File Name:python_basic 14
Author:冯鑫
Date:2021/11/19-10:32
==========================
"""
'''
本章讲解：条件判断
'''
'''
条件判断分为但分支语句,双分支语句和多分语句

单分支语句语法：
if 条件：
    语句块
    
如果条件成立(True)则执行语句块，反之不成立（False）则不执行语句块    
'''

# 案例1
age = 41
if age > 40:
    print('已经到中年了')  # 这一行是属于这个if判断的语句快，前面有4个空格或者一个Tab,python里面有严格的缩进规则

print('我是巴菲特')  # 注意：这行代码不属于上面这个if的语句快，属于这个文件全局的一段代码

# 案例2
date = '星期六'
if date == '星期六':
    print('不用上课')
    print('开心的很')

# date=input('请输入今天是星期几：')
if date == '星期六' or date == '星期天':
    print('今天放假')
    print('去哪玩呢')

# 案例2优化
# date=input('请输入今天是星期几：')
if date in ('星期六', '星期日'):
    print('今天放假,去小岛上玩')

print('无论if判断是否执行，这一句都会打印出来')

# 小练习：校验登录用户名和密码
# usename = input('请输入登录名:')
# password = input('请输入密码:')
# if usename == 'a123456' and password == 'a123456':
#     print('登录成功')
# else :
#     print('用户名或者密码错误')

'''
双分支语句语法：
if 条件：
    语句块1
else:
    语句块2
如果条件成立，则执行语句块1，如果条件不成立则执行语句块2    


    
'''
# 双分支案列1：
# tianqi=input('请输入天气：')
# if tianqi=='好':
#     print('晒被子')
# else:
#     print('睡觉')

# 双分支案列2：如果今天是周六或者周日就出去玩，其他时间去上课
# date=input('今天是星期几：')
# if date in ('星期六','星期天'):
#     print('今天是{}，我要出去玩'.format(date))
# else :
#     print('今天是{}，我要上课'.format(date))

# 双分支案例3：从控制台输入一个整数判断是奇数还是偶数
num = int(input('请输入一个整数：'))

# if num %2 ==1:
# print('%d是奇数'% num)
# else:
# num %2 ==0
# print('{}num是偶数'.foamat(num))

# if num%2:
#     print('%d是奇数'%num)
# else:
#     print('{}是偶数'.fomat(num))
