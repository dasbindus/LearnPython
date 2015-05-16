#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: sendmail_inline.py


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# from_addr = raw_input('From: ')
from_addr = 'bai123donggood@163.com'
password = raw_input('bai123donggood@163.com \n---> Password: ')
# to_addr = raw_input('To: ')
to_addr = '14210720136@fudan.edu.cn'
# smtp_server = raw_input('SMTP server: ')
smtp_server = 'smtp.163.com'


msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python Learner <%s>' % from_addr)
msg['To'] = _format_addr(u'Jack Bai <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()


# add MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello, Saber!</h1>' +
'<p><img src="cid:0"></p>' +
'</body></html>', 'html', 'utf-8'))


# add file:
with open('/home/baidong/workspaces/python/emailTest/test.jpg', 'rb') as f:
	mime = MIMEBase('image', 'jpg', filename='test.jpg')
	mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()