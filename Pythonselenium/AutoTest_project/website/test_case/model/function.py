'''
---------------------------
File Name:function
Author:FENGXIN
date:2022/3/31-9:47

---------------------------

'''
from selenium import webdriver
import os
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题



def insert_img(driver,filename):
    # 获取当前模块所在路径
    function_path = os.path.dirname(__file__)
    print(function_path)
    # 获取test_case目录
    base_dir = os.path.dirname(function_path)
    print(base_dir)
    # 将路径转化为字符串
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')  # 转换成相对路径

    print(base_dir)
    base = base_dir.split('/website')[0] # 获取项目文件的根目录路径
    print(base)
    # 指定截图存放路径
    filepath = base + '/website/test_report/screenshot/' + filename
    print(filepath)
    driver.get_screenshot_as_file(filepath)




def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名密码
    user = "m15161039042@163.com"
    password = "XGKUFEMVUNWJGXNU"

    # 发送和接收邮箱
    sender = "m15161039042@163.com"
    receives = ["m15161039042@126.com", '1126731010@qq.com']

    # 发送邮件主题和内容
    subject = 'Web Selenium 自动化测试报告'

    # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send Email end!")


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.png')
    driver.quit()
