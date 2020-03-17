#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com"  # 设置的邮件服务器host必须是发送邮箱的服务器，与接收邮箱无关。
mail_user = "2441086385@qq.com"  # qq邮箱登陆名
mail_pass = "zedzzipvcnzseaai"  # 开启smtp服务的时候并设置的授权码，注意！不是QQ密码。

sender = '2441086385@qq.com'  # 发送方qq邮箱
# receivers = ['xxx@qq.com']  # 接收方qq邮箱

def smtpEmail(receivers, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("戴林峰是猪", 'utf-8')  # 设置显示在邮件里的发件人
    message['To'] = Header("me", 'utf-8')  # 设置显示在邮件里的收件人

    subject = '今日打卡报告'
    message['Subject'] = Header(subject, 'utf-8')  # 设置主题和格式

    try:
        smtpobj = smtplib.SMTP_SSL(mail_host, 465)  # 本地如果有本地服务器，则用localhost ,默认端口２５,腾讯的（端口465或587）
        smtpobj.set_debuglevel(1)
        smtpobj.login(mail_user, mail_pass)  # 登陆QQ邮箱服务器
        smtpobj.sendmail(sender, receivers, message.as_string())  # 发送邮件
        print("邮件发送成功")
        smtpobj.quit()  # 退出
    except smtplib.SMTPException as e:
        print("Error:无法发送邮件")
        print(e)


# if __name__ == '__main__':
#     receivers = ['3104869949@qq.com']
#     smtpEmail(receivers, '发送测试-戴林峰是猪')