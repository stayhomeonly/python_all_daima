"""
=========================
File Name:logger02
Author:冯鑫
Date:2021/12/7-12:30
==========================
"""
from day16.log_utils import logger

try:
    num = input('请输入除数:')
    res = 50 / int(num)
    print(res)
except Exception as e:
    logger.error('该方法异常')  # 记录错误信息到文件
    logger.exception(e)  # 记录报错信息的对战回溯
else:
    logger.info('该方法异常')
