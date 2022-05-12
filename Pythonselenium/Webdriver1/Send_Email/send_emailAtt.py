'''
---------------------------
File Name:send_email_file
Author:FENGXIN
date:2022/3/28-16:02

---------------------------

'''
'''
发送带附件的邮件
案例：发送E:\Python_script\目录下 logo.png图片文件到指定的邮箱
'''
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.mime.multipart import MIMEMultipart  # 用于传送附件

# 发送邮箱服务器
smtpserver = 'smtp.163.com'

# 发送邮箱用户名密码
user = "m15161039042@163.com"
password = "XGKUFEMVUNWJGXNU"
# 发送和接收邮箱
sender = "m15161039042@163.com"
receives = ["m15161039042@126.com", '1126731010@qq.com']

# 发送邮件主题和内容
subject = 'Web Selenium 附件发送测试'
content = '<html><h1 style="color:red">我要自学网，自学成才!</h1></html>'

# 构造附件内容
send_file = open(r"C:\Users\FENG\Desktop\图片.jpg", 'rb').read()

att = MIMEText(send_file, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="logo.png"'

# 构建发送与接收信息
msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
msgRoot['subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = ','.join(receives)
msgRoot.attach(att)

# SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

# HELO 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录邮箱服务器用户名和密码
smtp.login(user, password)

print("Start send email...")

smtp.sendmail(sender, receives, msgRoot.as_string())

smtp.quit()
print("Send End！")
