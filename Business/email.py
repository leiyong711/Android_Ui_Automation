# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:34
# Email: leiyong711@163.com

import datetime
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def mail():
    # sender = '18216060753@139.com'       # 发件人1804882096@qq.com
    sender = 'leiyong711@aliyun.com'  # 发件人1804882096@qq.com
    receivers = 'leiyonghn@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱leiyong711@163.com
    receivers1 = 'leiyong711@163.com'
    my_pass = 'leiyong711'  # 授权码'ibiaowujreplcbhf'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Last_indulge", 'utf-8')  # 发件人名字Last indulge
    message['To'] = Header(receivers, 'utf-8')  # 收件人名字
    subject = '自动化测试报告1'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    timeStr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    directory1 = '..\\report\\' + timeStr[:10] + '\\' + timeStr[11:] + '\\log\\'
    directory = os.listdir(directory1)
    print directory
    for i in range(len(directory)):
        if str(directory[i]).find(".xls") != -1:
            the_attachment = directory[i]
    nei = '以下是%s分执行后的测试版报告，该附件包含：' \
          '\n   • 测试信息汇总：%s' \
          '\n   • 用例执行结果：Case_report.html' \
          '\n   • Appium运行日志：appium.log' \
          '\n   • Python运行日志：mylog.log' % (str(datetime.datetime.now())[:-7], the_attachment)
    message.attach(MIMEText(nei, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 测试汇总 文件
    att1 = MIMEText(open(directory1 + the_attachment, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename=' + the_attachment     # 附件别名
    message.attach(att1)

    # 构造附件2，传送当前目录下的 html测试报告 文件
    the_attachment2 = 'Case_report.html'
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    att2 = MIMEText(open('..\\report\\' + timestr[:10] + '\\' + timestr[11:] + '\\Case_report\\' +
                         the_attachment2, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename='+the_attachment2
    message.attach(att2)

    # 构造附件3，传送当前目录下的 appium运行日志 文件
    the_attachment3= "appium.log"
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    att3 = MIMEText(open('..\\report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\' +
                         the_attachment3, 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename='+the_attachment3
    message.attach(att3)

    # 构造附件4，传送当前目录下的 python错误日志 文件
    the_attachment4 = 'mylog.log'
    # timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    att4 = MIMEText(open('..\\report\\log\\' +
                         the_attachment4, 'rb').read(), 'base64', 'utf-8')
    att4["Content-Type"] = 'application/octet-stream'
    att4["Content-Disposition"] = 'attachment; filename=' + the_attachment4
    message.attach(att4)

    try:
        server = smtplib.SMTP("smtp.aliyun.com", 25)  # 发件人邮箱中的'SMTP'服务器，端口是25
        server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(sender, receivers1, message.as_string())
        # 关闭连接
        server.quit()
        print "邮件发送成功"

    except smtplib.SMTPException:
        print "无法发送邮件"


if __name__ == '__main__':
    mail()
