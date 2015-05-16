#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: sendmail_multipart.py

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((\
		Header(name, 'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# from_addr = raw_input('From: ')
from_addr = 'bai123donggood@163.com'
password = raw_input('bai123donggood@163.com \n---> Password: ')
# to_addr = raw_input('To: ')
to_addr = '14210720136@fudan.edu.cn'
# smtp_server = raw_input('SMTP server: ')
smtp_server = 'smtp.163.com'

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/home/baidong/workspaces/python/emailTest/broken_bike.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='broken_bike.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='broken_bike.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()