"""
#@Time：2022/5/11-10:40
#@file：maildemo
#@Project:python_basic05.py
#@Content:

"""
# 需要使用到SMTPLIB库，来进行邮箱的连接

# 邮箱属性的配置
mailserver = 'smtp.qq.com'  # 邮箱服务端URL
userName_SendMail = "1126731010@qq.com"  # 发件人
unserName_AuthCode = 'xpzljjypzobijbai'  # 邮件授权码
receive_mail = ["1126731010@qq.com",
                'm15161039042@163.com']  # 邮箱收件人如果后面还需要添加其他人，加个逗号，写入邮箱账号
