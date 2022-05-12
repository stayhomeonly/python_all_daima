"""
=========================
File Name:logger01
Author:冯鑫
Date:2021/12/7-9:49
==========================
"""
'''
log/日志:用来记录软件运行的轨迹.我们可以把需要记录的内容记录成文件,方便以后查看
日志的级别:
debug: 记录详细的信息,主要用来调试
info:记录正确情况下,重要的日志
waring:记录告警信息
error:记录错误信息
'''

# 第一步:导入logging
import logging

# 第二部:创建日志对象
logger = logging.getLogger('logging')  # 括号里面name可以为空
logger.setLevel('DEBUG')  # 设置默认的日志级别DEBUG,代表获取DEBUG及DEBUG级别以上的日志

# 第三步:设置输出方向
# 输出到控制台,并且级别INFO,代表INFO及INFO级别以上的内容
sh1 = logging.StreamHandler()
sh1.setLevel('INFO')  # 代表数据INFO及INFO级别以上的内容

# 输出到./info.log 文件,并且内容追加写入,并且级别INFO及INFO级别以上的内容
sh2 = logging.FileHandler(filename=r'./info.log', mode='a', encoding='utf-8')
sh2.setLevel('INFO')

# 输出到./error.log 文件,并且内容追加写入,并且级别ERROR及ERROR级别以上的内容
sh3 = logging.FileHandler(filename=r'./error.log', mode='a', encoding='utf-8')
sh3.setLevel('ERROR')

# 第四步:添加输出方向到logger对象

logger.addHandler(sh1)
logger.addHandler(sh2)
logger.addHandler(sh3)

# 第五步:指定日志输出格式,可以直接百度
frm_str = '%(asctime)s-[%(filename)s - %(lineno)d]-%(levelname)s:%(message)s'
my_fmt = logging.Formatter(frm_str)  # 设置样式
sh1.setFormatter(my_fmt)
sh2.setFormatter(my_fmt)
sh3.setFormatter(my_fmt)

# 第六步:如何使用
logger.debug('debug级别以上的日志信息')  # 代表我们需要在此处记录debug级别的信息
logger.debug('info级别以上的日志信息')  # 代表我需要此处记录info级别的信息
logger.warning('waring级别以上的日志信息')
logger.error('error级别以上的日志信息')
