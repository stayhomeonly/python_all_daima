"""
--------------------------------
@Time    :  2022/2/28 - 15:50
@Author  :  Lee
@File    :  log_utils
--------------------------------
"""
import logging
from autotest.comms.constants import INFO_FILE, ERROR_FILE


def get_logger():
    # 第二步:创建日志对象
    logger = logging.getLogger()
    logger.setLevel("DEBUG")  # 代表获取DEBUG及DEBUG级别以上的内容

    # 第三步:设置输出方向
    # 日志输出到控制台,级别是INFO及INFO级别以上的内容
    sh1 = logging.StreamHandler() # 文件流的输出
    sh1.setLevel("INFO")  # 级别是DEBUG及DEBUG级别以上的内容

    # 输出 ./info.log文件,并且内容为追加写入,级别是INFO及INFO级别以上的内容，这种是写到文件中的
    sh2 = logging.FileHandler(filename=INFO_FILE, mode='a', encoding='utf-8')
    sh2.setLevel("INFO")  # 级别是INFO及INFO级别以上的内容

    # 输出 ./error.log文件,并且内容为追加写入,级别是ERROR及ERROR级别以上的内容
    sh3 = logging.FileHandler(filename=ERROR_FILE, mode='a', encoding='utf-8')
    sh3.setLevel("ERROR")  # 级别是ERROR及ERROR级别以上的内容

    # 第四步: 添加输出方向到logger对象
    logger.addHandler(sh1)
    logger.addHandler(sh2)
    logger.addHandler(sh3)

    # 第五步: 指定日志输出格式
    fmt_str = '%(asctime)s - [%(filename)s - %(lineno)d] - %(levelname)s:%(message)s'
    my_fmt = logging.Formatter(fmt_str)  # 设置样式
    sh1.setFormatter(my_fmt)
    sh2.setFormatter(my_fmt)
    sh3.setFormatter(my_fmt)

    return logger


logger = get_logger()
