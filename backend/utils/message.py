#!/usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="Tsingora User Register"):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["Tsingora",'Tsingora@126.com'])
    msg['Subject'] = subject

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("Tsingora@126.com", "csm0212")
    server.sendmail('Tsingora@126.com', email_list, msg.as_string())
    server.quit()

