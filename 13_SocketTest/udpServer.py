#! /usr/bin/env python
# Filename: udpServer.py

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind
s.bind(('10.12.134.125', 9998))
print 'Bind UDP on 9998...'

while True:
	# receive data
	data, addr = s.recvfrom(1024)
	print 'Receive from %s:%s.' % addr
	s.sendto('Hello, %s!' % data, addr)