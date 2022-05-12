"""
=========================
File Name:python_basic32
Author:冯鑫
Date:2021/11/25-15:46
==========================
"""

'''
通过流操作文件：读和写
'''
'''1.文件内容读取   '''
# 第一步：打开文件（注意在路径中，有绝对路径【一般从根目录开始的路径，比如：D：\tools]和相对路径【
# 相当于当前文件的路径】
# 打开相对路径下的test.txt文件，并且读取操作（r代表只读），以uft8编码格式进行识别
fr = open(r'./test.txt', mode='r', encoding='utf8')
# 第二步：文件内容读取
res = fr.read()  # 读取文件所有内容
# res=fr.readline()#读取所有内容，但是会把每一行内容读取列表里，包括换行符
# res=fr.readlines()#读取所有内容，但是会把每一行的内容读取列表里，包括换行符
print(res)
# 第三步：关闭流
fr.close()

'''
2.文件的写入 a 代表追加写入，会在以前的内容基础上增加内容 w 代表覆盖式写入，会把
以前的内容覆盖掉
w和a模式当文件不存在时，都会创建合格文件

'''
fw = open(r'.\test.txt', mode='a', encoding='utf8')
fw.write('\n天生我材必有用，千金散尽还复来')
fw.write('\n仰天大笑出门去，我辈岂是蓬篙人')
fw.close()

print(fw)

fw1 = open(r'.\test.txt', mode='r', encoding='utf8')
t = fw1.read
print(t)

'''
3.传统方式的读和写：好处，不用手写刷新或关闭
'''
with open(r'./test.txt', mode='r', encoding='utf8') as fr:
    print(fr.read())

# 读出出师表
gw = open(r'.\test.txt', mode='r', encoding='utf8')

res1 = gw.read()
print(res1)
gw.close

gw2 = open(r'.\test.txt', mode='a', encoding='utf8')
gw2.write('\n鹅鹅鹅,曲项向天歌')
gw2.write('\n白毛浮绿水，红掌拨清波。')

print(gw2)
gw2.close

'''
3.传统方式的读和写：好处，不用手写刷新或关闭
'''
with open(r'./test.txt', mode='r', encoding='utf8') as fr:
    print(fr.read())

with open(r'./test.txt',mode='w',encoding='utf8') as fw:
    print(fw.write('好好学习，天天向上'))
