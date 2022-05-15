"""
#@Time：2022/5/14-22:20
#@file：send_email
#@Project:python_basic05.py
#@Content:

"""
import datetime
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 发文件和word方法都验证过了
class emailsend:
    def sendfile(self, content):  # 带附件的发送
        sender = '1126731010@qq.com' # 发件人
        receiver = '1126731010@qq.com' # 收件人邮箱
        smtpserver = 'smtp.qq.com'   # 邮箱服务端URL
        username = '1126731010@qq.com'# 发件人邮箱
        password = 'xpzljjypzobijbai'#'邮件发送的授权码'
        mail_title = '主题：这是带附件的邮件'

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = "{}".format(sender)  # 发送者
        message['To'] = ",".join(receiver)  # 接收者
        message['Subject'] = Header(mail_title, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件1（附件为TXT格式的文本,excel）
        # att1 = MIMEText(open('冯鑫.txt', 'rb').read(), 'base64', 'utf-8')  # 文件路径是这个代码附近的文件
        # att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="冯鑫.txt"'
        # message.attach(att1)

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(open('消息中台问题排查.docx', 'rb').read())
        att.add_header('Content-Disposition', 'attachment', \
                       filename=Header('消息中台问题排查.docx', 'gbk').encode())
        encoders.encode_base64(att)
        message.attach(att) # 这个txt文件没有问题，如果想换其他格式用改一下open后面名字

        # # 构造附件2（附件为JPG格式的图片）
        # att2 = MIMEText(open('IMG_8455.PNG', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="wangzhe.jpg"'
        # message.attach(att2)

        # # 构造附件3（附件为HTML格式的网页）
        # att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')
        # att3["Content-Type"] = 'application/octet-stream'
        # att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
        # message.attach(att3)

        try:
            smtpObj = smtplib.SMTP_SSL(smtpserver, 465)
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, receiver, message.as_string())
            print("mail has been send successfully")
            e = "邮件发送成功！！！"
            smtpObj.quit()
        except smtplib.SMTPException as error:
            e = str(error)
        except Exception as e:
            print('邮件发送失败   ' + str(e) + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return

    def sendtext(mail_host, mail_user, mail_pass, receivers, title, content):
        mail_host = mail_host
        mail_user = mail_user
        mail_pass = mail_pass

        sender = mail_user
        receivers = ['接收人邮箱地址']  # 接收人 默认为百草味邮箱

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        content = content  # 发送邮件内容
        title = title  # 设置主题
        # subject = 'Python SMTP 邮件测试'
        message = MIMEText(content, 'plain', 'utf-8')  # 内容，格式，编码
        msg = MIMEMultipart()  # 带附件是实例
        message['From'] = "{}".format(sender)  # 发送者
        message['To'] = ",".join(receivers)  # 接收者
        message['Subject'] = title  # 主题

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("mail has been send successfully")
            print('邮件发送成功' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            smtpObj.quit()
        except smtplib.SMTPException as error:
            print(str(error))
        except Exception as e:
            print('邮件发送失败' + str(e) + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        if '__name__' == '__main__':
            print()


es = emailsend()
# es.sendfile('mail has been send successfully' + '\n' + "这个是附件")
es.sendfile('这是今天排查的错误内容' + '\n' + "这个是附件")
# 最后一行就是自己写的content内容
