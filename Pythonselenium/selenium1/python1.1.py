'''
---------------------------
File Name:python1.1
Author:FENGXIN
date:2022/2/25-22:04

---------------------------

'''
import csv

"""
打开文件
使用python内置的办法open()可以打开文件
file object = open(file_name,[,acess_mode][,buffering])
file_name :file_name 变量是一个包含你要访问的文件名称 的字符串值

acess_mode:acess_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下
的完全列表。这个参数是非强制的，默认文件访问模式为只读（r）.

buffering :如果buffering的值被设为0，就不会有寄存。如果buffering 的值取1，访问文件是会寄
存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲
大小则为系统默认

文件读取
line = f.read() read()每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
line1 =  f.readline() readline() 每次读取一行
line2 = f.readlines() readlines()一次性读取文件所有行，自动将文件内容分析成一个行的列表，
该列表可以有python的for ... in ....结构进行处理。
f.close() 关闭文件

 spilt()方法语法：
str.split(str="",num=string.count(str))
参数
 str --分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
 num --分割字数

"""
# f = open("1.txt", mode='r')
# lines = f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split(',')[1])


# CSV读写的操作
# import  csv
#
# csv_file = csv.reader(open('stu.csv','r'))
# print(csv_file)
#
# for stu in csv_file:
#     print(stu[0])

stu = ['Marry', 28, 'ChangSha']
stu1 = ['Rom', 23, 'Chengdu']
# 打开文件
out = open("stu.csv", mode='a', newline="") # a 用于追加，新写的内容将会被写入到已有内容之后，W只是写入，覆盖
# 设定写入模式
csv_write = csv.writer(out, dialect='excel')
# 写入具体的的数字
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("Write file over")
