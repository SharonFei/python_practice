# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
msgRoot = MIMEMultipart('related')


'''
from_addr = 
password = 
to_addr = 
smtp_server = smtp.163.com
'''

# 添加一个MIMEmultipart类，处理正文及附件
msg = MIMEMultipart()
mail_msg = '''
<p>你好，我是XXX，这个是我通过python发送的邮件</p>
<p> Here is the<a href="http://www.python.org">link</a>you wanted.</p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
'''
text = MIMEText(mail_msg, 'html', 'utf-8')
msg['From'] = Header('matchafei')
msg['To'] = Header(u'matchafei ')
msg['Subject'] = Header('你好，我是XXX，这个是我通过python发送的邮件', 'utf-8')


# 指定图片为当前目录
fp = open('D:/python/picture/picture.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 将内容附加到邮件主体中
msg.attach(text)
msg.attach(msgImage)


try:
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败')
