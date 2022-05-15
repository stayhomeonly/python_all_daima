"""
#@Time：2022/5/11-10:40
#@file：maildemo
#@Project:python_basic05.py
#@Content:

"""
import smtplib  # 需要使用到SMTPLIB库，来进行邮箱的连接
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
# 处理邮件附件需要导入其他的包 MIMEMultipart Header MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 处理内容的库，email.mime

# 邮箱属性的配置
mailserver = 'smtp.qq.com'  # 邮箱服务端URL
userName_SendMail = "1126731010@qq.com"  # 发件人
unserName_AuthCode = 'xpzljjypzobijbai'  # 邮件授权码
receive_mail = ["1126731010@qq.com"]  # 邮箱收件人如果后面还需要添加其他人，加个逗号，写入邮箱账号

# 发送一封简单的邮件
# content = "这是一封纯粹的文本信息内容"
#
# email = MIMEText(content, 'plain', 'utf-8')  # 纯文本形式的邮件内容定义
#
# email['Subject'] = '邮件主题'  # 定义邮件主题
#
# email['From'] = userName_SendMail  # 发件人
# email['To'] = "1126731010@qq.com"  # 收件人
# # email['To']=','.join(receive_mail) # 如果多个收件人建议这种

# # 发送一封html的内容的邮件
# content="""
# <p>这是一封HTML文本的邮件</p>
# <p><a href="http://www.baidu.com">点击这里就送个锤子</a></p>
# """
# email=MIMEText(content,'HTML','utf-8') # 纯文本形式的邮件内容定义
#
# email['Subject']='邮件主题_HTML'  # 定义邮件主题
#
# email['From']=userName_SendMail # 发件人
# email['To']="1126731010@qq.com" # 收件人
# # email['To']=','.join(receive_mail) # 如果多个收件人建议这种

# 邮件中发送附件
# 附件配置邮箱


email = MIMEMultipart()


email['Subject'] = '附件'  # 定义邮件主题

email['From'] = userName_SendMail  # 发件人
email['To'] = "1126731010@qq.com"  # 收件人
# email['To']=','.join(receive_mail) # 如果多个收件人建议这种
# 非图片附件
att = MIMEBase('application', 'octet-stream')
att.set_payload(open('冯鑫.txt', 'rb').read())
att.add_header('Content-Disposition', 'attachment', \
               filename=Header('冯鑫.txt', 'gbk').encode())
encoders.encode_base64(att)
email.attach(att)

# 图片附件
att1 = MIMEBase('application', 'octet-stream')
att1.set_payload(open('毛选.jpg', 'rb').read())
att1.add_header('Content-Disposition', 'attachment', \
               filename=Header('毛选.jpg', 'gbk').encode())
encoders.encode_base64(att1)
email.attach(att1)


# 发送邮件

smtp = smtplib.SMTP_SSL(mailserver, port=465) # 非QQ邮箱，一般使用SMTP即可，不需要有SSL

smtp.login(userName_SendMail, unserName_AuthCode)

smtp.sendmail(userName_SendMail, ','.join(receive_mail), email.as_string())

smtp.quit()

print("邮件发送成功")
