#! /usr/bin/env python

import socket


# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect
s.connect(('www.sina.com.cn', 80))
# send a GET request
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnectoin: close\r\n\r\n')

# receive data
buf = []
while True:
	d = s.recv(1024)
	if d:
		buf.append(d)
	else:
		break
data = ''.join(buf)

# close connetion
s.close()

header, htmlSrc = data.split('\r\n\r\n', 1)
print header
with open('sina.html', 'wb') as f:
	f.write(data)