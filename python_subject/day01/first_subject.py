"""
#@Time：2022/5/15-22:18
#@file：first_subject
#@Project:git_all_python_daima
#@Content:

"""
'''
将华氏温度转换为摄氏温度
F = 1.8C + 32
'''
# 华氏温度
f = float(input('请输入华氏温度:'))
# 摄氏度计算
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
