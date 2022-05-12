"""
#@Time：2022/5/10-17:12
#@file：logging_test
#@Project:python_basic05.py
#@Content:

"""
'''
%(levelno)s	打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径
%(filename)s	打印当前执行程序名称
%(funcName)s	打印日志的当前函数
%(lineno)d	打印日志的当前行号
%(asctime)s	打印日志的时间
%(thread)d	打印线程id
%(threadName)s	打印线程名称
%(process)d	打印进程ID
%(message)s	打印日志信息

'''
import logging

# logging.basicConfig(level=logging.DEBUG)  # 调用日志级别输出
logging.basicConfig(level=logging.INFO,filename='runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d '
                           '%(levelname)s %(message)s]') # 更改级别代表输出哪个级别之上的
# 简单演示
logging.debug('debug info')
logging.info('hello 51zxw')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')
