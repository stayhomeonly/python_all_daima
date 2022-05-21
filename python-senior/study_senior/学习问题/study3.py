"""
#@Time：2022/5/16-22:19
#@file：study3
#@Project:python-senior
#@Content:

"""
# 求'a'出现的字数
a = "abcdjafakghiaogiaghehuhui"
print(a.count('a'))
count1=0
for i in range(len(a)-1):
    if a[i]=="a":
        count1 += 1
print(count1)

