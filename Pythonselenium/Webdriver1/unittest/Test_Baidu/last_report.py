'''
---------------------------
File Name:last_report
Author:FENGXIN
date:2022/3/28-20:07

---------------------------

'''
import os  # 用于访问操作系统功能的模块

report_dir = './test_report'  # 报告存放位置

lists = os.listdir(report_dir)

print(lists)
#按时间顺序对该目录文件夹下面的文件进行排序
lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

print("the latest report is " + lists[-1])
#输出最新报告的路径
file = os.path.join(report_dir, lists[-1])
print(file)
