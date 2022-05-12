'''
---------------------------
File Name:send_emailMulti
Author:FENGXIN
date:2022/3/28-11:12

---------------------------

'''
# 向多个人发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户名密码
user = "m15161039042@163.com"
password = "XGKUFEMVUNWJGXNU"
# 发送和接收邮箱
sender = "m15161039042@163.com"
receives = ["m15161039042@126.com", '1126731010@qq.com']
# 发送邮件主题和内容
subject = "Web selenium 自动化测试报告"
content = '<html><h1 style="color:red">我要自学网，自学成才!</h1></html>'
# HTML邮件正文
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'm15161039042@163.com'
msg['To'] = ','.join(receives)
# SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)
# HELO 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录邮箱服务器用户名和密码
smtp.login(user, password)

print("开始发送邮件...")
smtp.sendmail(sender, receives, msg.as_string())
smtp.quit()
print("邮件发送完成！")
