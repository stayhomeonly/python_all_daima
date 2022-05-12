'''
---------------------------
File Name:study
Author:FENGXIN
date:2022/1/25-11:02

---------------------------

'''
# 列表中任意两个数相加等于50则返回True，否则False
list1 = [1, 3, 56, 34, 23, 49, 37, 2, 48]
print(list1.index(1))  # 代表list1中的1的下标位置


# for i in list1:
#     b = 50 - i
#     if b in list1:
#         print('true')
#         break
#     else:
#         print('False')
def adds(list1):
    for i in list1:
        for j in list1:
            if i + j == 50 and list1.index(i) != list1.index(j):
                # list1.index(i) != list1.index(j) 代表 i 的下标位置 不等于j的下标位置
                return True

    return False


print(adds(list1))
